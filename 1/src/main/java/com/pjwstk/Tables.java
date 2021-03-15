package com.pjwstk;

import java.util.Arrays;

public class Tables {

    int[] arr;

    public Tables() {
    }

    public Tables(int[] arr) {
        this.arr = arr;
    }

    public int sum(int[] arr){
        int sum = 0;
        for (int i = 0; i < arr.length; i++){
            sum += arr[i];
        }
        return sum;
    }

    public String toString(int[] arr){
        return Arrays.toString(arr);
    }

    public int[] addN(int[] arr, int n){
        int[] arr2 = new int[arr.length];
        for(int i = 0; i < arr.length; i++){
            arr2[i] = arr[i] + n;
        }
        return arr2;
    }

    public int[] reverse(int[] arr){
        int[] arr2 = new int[arr.length];
        for(int i = 0; i < arr.length; i++){
            arr2[i] = arr[(arr.length - 1) - i];
        }
        return arr2;
    }

    public boolean hasN(int[] arr, int n) {
        boolean exists = false;
        for (int i = 0; i < arr.length; i++){
            if (arr[i] == n) {
                exists = true;
                break;
            }
        }
        return exists;
    }

    public int[] replaceAll(int[] arr, int old, int nw){
        for (int i = 0; i < arr.length; i++){
            if(arr[i] == old) {
                arr[i] = nw;
            }
        }
        return arr;
    }

    public int[] sort(int[] arr){
        int[] arr2 = new int[arr.length];
        for(int i = 0; i < arr.length; i++){
            arr2[i] = arr[i];
        }
        bubbleSort(arr2);
        return arr2;
    }

    // https://stackoverflow.com/questions/11644858/bubblesort-implementation
    public static void bubbleSort(int[] list)
    {
        for(int i=0; i<list.length; i++)
        {
            for(int j=i + 1; j<list.length; j++)
            {
                if(list[i] > list[j])
                {
                    int temp = list[i];
                    list[i] = list[j];
                    list[j] = temp;
                }
            }

        }
    }
}
