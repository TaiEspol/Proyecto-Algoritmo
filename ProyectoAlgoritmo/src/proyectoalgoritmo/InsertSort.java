/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyectoalgoritmo;

/**
 *
 * @author Marbelisa
 */
public class InsertSort {
    
    public InsertSort(){
        
    }
    public static void insertionSortImperative(int[] input) {
        for (int i = 1; i < input.length; i++) { 
            int key = input[i]; 
            int j = i - 1;
            while (j >= 0 && input[j] > key) {
                input[j + 1] = input[j];
                j = j - 1;
            }
            input[j + 1] = key; 
        }
    }
}
