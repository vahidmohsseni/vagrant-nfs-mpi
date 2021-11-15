    #include<mpi.h>


    int main(int argc, char**argv)
    {
        
    MPI_Init(&argc,&argv);
    int myRank, size; 
    MPI_Comm_size(MPI_COMM_WORLD, &size); 
    MPI_Comm_rank(MPI_COMM_WORLD,&myRank);
    printf("Hello World, My rank is %d and size is %d processors\n", myRank, size);
    MPI_Finalize();
    return 0;
    }