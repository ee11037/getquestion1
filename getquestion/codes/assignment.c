#include<stdio.h>




typedef struct Point {

   float x;

   float y;

} point;




int main() {

   point A,B,P;

   A.x = 2.00, A.y = -5.00;

   B.x = 5.00, B.y = 2.00;

   int i,j,k;

   float a = 2.00/5.00, b = 3.00/5.00;

   float coordinate_matrix[2][2] = {{A.x, B.x}, {A.y, B.y}};

   float ratio_matrix[2][1] = {b, a};

   float Point_P[2][1] = {{0},{0}};

   for(i=0;i<2;i++){

       for(j=0;j<1;j++){

           for(k=0;k<2;k++){

               Point_P[i][j] += (coordinate_matrix[i][k] * ratio_matrix[k][j]);

           }

       }

   }

   P.x = Point_P[0][0], P.y = Point_P[1][0];

   FILE * file;

   file = fopen("output_points.txt", "w");

   if(file == NULL){

       printf("Error opening file..\n");

   }

   fprintf(file, "A(%0.2f , %0.2f)\n", A.x, A.y);

   fprintf(file, "B(%0.2f , %0.2f)\n", B.x, B.y);

   fprintf(file, "C(%0.2f , %0.2f)\n", P.x, P.y);

   fclose(file);

   return 0;

}
