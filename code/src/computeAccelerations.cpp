__device__ double atomicAdd_double(double *address, double val){
    unsigned long long int *address_as_ull = (unsigned long long int *)address;
    unsigned long long int old = *address_as_ull, assumed;

    do
    {
        assumed = old;
        old = atomicCAS(address_as_ull, assumed,
                        __double_as_longlong(val + __longlong_as_double(assumed)));
    } while (assumed != old);

    return __longlong_as_double(old);
}

__global__ void computeAccelerationsKernel(double *r_, double *a_, double *Pot, int N_){
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < N_ - 1){
        double f, rSqd;
        double rij[3];
        double rSqd3, rSqd7, rijf[3], sigma6 = 1.0, term1, term2;
        double local_a[] = {0.0,0.0,0.0}, ri[] = {r_[i*3],r_[i*3+1],r_[i*3+2]};

        Pot[i] = 0.0;
        for(int j = i+1; j < N_; j++){
            rij[0] = ri[0] - r_[j*3];
            rij[1] = ri[1] - r_[j*3+1];
            rij[2] = ri[2] - r_[j*3+2];
            rSqd = rij[0] * rij[0] +
                   rij[1] * rij[1] +
                   rij[2] * rij[2];

            rSqd3 = rSqd * rSqd * rSqd;
            rSqd7 = rSqd3 * rSqd3 * rSqd;
            f = (48 - 24 * rSqd3) / rSqd7;

            term2 = sigma6 / (rSqd * rSqd * rSqd);
            term1 = term2 * term2;
            Pot[i] += term1 - term2;

            rijf[0] = rij[0] * f;
            rijf[1] = rij[1] * f;
            rijf[2] = rij[2] * f;
            
            local_a[0] += rijf[0];
            local_a[1] += rijf[1];
            local_a[2] += rijf[2];
            
            atomicAdd_double(a_+j*3  , -rijf[0]);
            atomicAdd_double(a_+j*3+1, -rijf[1]);
            atomicAdd_double(a_+j*3+2, -rijf[2]);
        }
        atomicAdd_double(a_+i*3, local_a[0]);
        atomicAdd_double(a_+i*3+1, local_a[1]);
        atomicAdd_double(a_+i*3+2, local_a[2]);
    }
}

void computeAccelerationsCUDA(){
    for (int i = 0; i < N; i++){
        a[i][0] = a[i][1] = a[i][2] = 0;
    }

    double *d_r, *d_a, *d_P; // arrays na GPU: r, a e Potenciais
    double h_P[N];// arrays no host: output dos potenciais vindos da GPU

    cudaMalloc((void **)&d_a, N * 3 * sizeof(double));
    checkCUDAError("cudaMalloc 1");
    cudaMalloc((void **)&d_r, N * 3 * sizeof(double));
    checkCUDAError("cudaMalloc 2");
    cudaMalloc((void **)&d_P, N * sizeof(double));
    checkCUDAError("cudaMalloc 3");

    cudaMemcpy(d_a, a, N * 3 * sizeof(double), cudaMemcpyHostToDevice);
    checkCUDAError("cudaMemcpy 2");
    cudaMemcpy(d_r, r, N * 3 * sizeof(double), cudaMemcpyHostToDevice);
    checkCUDAError("cudaMemcpy 2");

    int threadsPerBlock = 512;
    int nBlocks = (N + threadsPerBlock - 1) / threadsPerBlock;

    computeAccelerationsKernel<<<nBlocks, threadsPerBlock>>>(d_r, d_a, d_P, N);

    cudaMemcpy(a, d_a, N * 3 * sizeof(double), cudaMemcpyDeviceToHost);
    checkCUDAError("cudaMemcpu 1");
    cudaMemcpy(h_P, d_P, N * sizeof(double), cudaMemcpyDeviceToHost);
    checkCUDAError("cudaMemcpu 2");

    // Redução do array dos potenciais
    P = 0.0;
    for (int i = 0; i < N - 1; i++){
        P += h_P[i];
    }
    P *= 8 * epsilon;

    cudaFree(d_a);
    cudaFree(d_r);
    cudaFree(d_P);
}