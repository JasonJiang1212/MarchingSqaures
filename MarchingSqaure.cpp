#include <iostream>
#include <fstream>
#include <cstdlib>

int main(int argc, const char * argv[]) {
    
    
    std::ifstream file { "BinaryImage.txt" };
    if (!file.is_open()) return -1;
    
    int my_array [10][12]{};
    for (int i =0; i< 10; i++) {
        for (int j=0; j < 12; j++) {
            file >> my_array[i][j];
            //std::cout << my_array[i][j] <<" ";
        }
        //std::cout << "\n";
    }
    
    int newArray [10][12]{};
    bool stop=false;
    int i=0;
    int j=0;
    int initalI=0;
    int initialJ =0;
    bool set = false;
    while (stop == false) {
        
        
        if((i<9) && (j<11)) {
            
            int num0 = my_array[i][j];
            int num1 = my_array[i][j+1];
            int num2 = my_array[i+1][j+1];
            int num3 = my_array[i+1][j];
            
            if (((num0==1) || (num1==1) || (num2==1) || (num3==1)) && (set == false)) {
                 initalI = i;
                 initialJ = j;
                set = true;
            }
            
            if ( (num0 ==0) && (num1 ==0) && (num2 ==0) && (num3 ==0)  ) {
                
                j=j+1;
            }
            
            if ( (num0 ==0) && (num1 ==1) && (num2 ==0) && (num3 ==0)  ) {
                newArray[i][j+1]=1;
                j=j+1;
            }
            
            
            if ( (num0 ==0) && (num1 ==1) && (num2 ==1) && (num3 ==0)  ) {
                newArray[i][j+1]=1;
                newArray[i+1][j+1]=1;
                i=i+1;
                
                
            }
            if ( (num0 ==0) && (num1 ==0) && (num2 ==1) && (num3 ==0)  ) {
                
                newArray[i+1][j+1]=1;
                i=i+1;
            }
            
            if ( (num0 ==1) && (num1 ==1) && (num2 ==0) && (num3 ==0)  ) {
                newArray[i][j]=1;
                newArray[i][j+1]=1;
                
                j=j+1;
            }
            
            if ( (num0 ==1) && (num1 ==0) && (num2 ==0) && (num3 ==0)  ) {
                
                newArray[i][j]=1;
                i=i-1;
            }
            if ( (num0 ==1) && (num1 ==0) && (num2 ==0) && (num3 ==1)  ) {
                 newArray[i][j]=1;
                 newArray[i+1][j]=1;
                 i=i-1;
            }
            if ( (num0 ==0) && (num1 ==0) && (num2 ==0) && (num3 ==1)  ) {
                
                newArray[i+1][j]=1;
                j=j-1;
                
            }
            if ( (num0 ==0) && (num1 ==0) && (num2 ==1) && (num3 ==1)  ) {
                 newArray[i+1][j+1]=1;
                 newArray[i+1][j]=1;
                 j=j-1;
            }
            
            if ( (num0 ==1) && (num1 ==0) && (num2 ==1) && (num3 ==1)  ) {
                
                newArray[i][j]=1;
                newArray[i+1][j+1]=1;
                i=i-1;
            }
            if ( (num0 ==0) && (num1 ==1) && (num2 ==1) && (num3 ==1)  ) {
                newArray[i][j+1]=1;
                newArray[i+1][j]=1;
                j=j-1;
            }
            
            if ( (num0 ==1) && (num1 ==1) && (num2 ==1) && (num3 ==0)  ) {
                
                newArray[i][j]=1;
                newArray[i+1][j+1]=1;
                i=i+1;
            }
            
            if ( (num0 ==1) && (num1 ==1) && (num2 ==0) && (num3 ==1)  ) {
                
                newArray[i][j+1]=1;
                newArray[i+1][j]=1;
                j=j+1;
            }
            if ( (num0 ==1) && (num1 ==0) && (num2 ==1) && (num3 ==0)  ) {
                newArray[i][j+1]=1;
                newArray[i+1][j+1]=1;
                i=i-1;
            }
            if ( (num0 ==0) && (num1 ==1) && (num2 ==0) && (num3 ==1)  ) {
                
                newArray[i][j+1]=1;
                newArray[i+1][j]=1;
                j=j-1;
                
            }
            if ( (num0 ==1) && (num1 ==1) && (num2 ==1) && (num3 ==1)  ) {
                
                stop=true;
            }
            if((i==initalI) && (j==initialJ)){
                stop=true;
            }
        
    }
    }
    for (int i =0; i< 10; i++) {
        for (int j=0; j < 12; j++) {
            file >> my_array[i][j];
            std::cout << newArray[i][j] <<" ";
        }
        std::cout << "\n";
    }
  
    
    while (true);
    return 0;
}
