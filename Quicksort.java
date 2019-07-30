import java.util.Scanner;
class Quicksort{
    public static void main(String arg[])
    {
        System.out.println("enter the size of the array");
        Scanner sc =new Scanner(System.in);
        int n=sc.nextInt();
        int arr[]=new int[n];
        for(int i=0;i<n;i++)
        {
            arr[i]=sc.nextInt();
        }
        quicksort(arr,0,n-1);
        for(int i=0;i<n;i++)
        {
            System.out.println(arr[i]);
        }

    }
    static void quicksort(int arr[],int start,int end)
    {
        if(start<end)
        {
        int q=partition(arr,start,end);
        quicksort(arr,start,q-1);
        quicksort(arr,q+1,end);
        }
    }
    static int partition(int arr[],int start,int end)
    {
        int x=arr[end];
        int i=start-1;
        for(int j=start;j<end;j++)
        {
            if(arr[j]<x)
            {
                i=i+1;
                int ex=arr[i];
                arr[i]=arr[j];
                arr[j]=ex;
            }
        }
        int ex=arr[i+1];
        arr[i+1]=arr[end];
        arr[end]=ex;
        return i+1;
    }
}