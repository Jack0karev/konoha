{\rtf1\ansi\ansicpg1251\cocoartf2511
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;\f1\fnil\fcharset0 Menlo-Bold;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red241\green241\blue241;\red115\green0\blue2;
\red0\green0\blue109;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c95686\c95686\c95686;\cssrgb\c53333\c0\c0;
\cssrgb\c0\c0\c50196;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl220\partightenfactor0

\f0\fs20 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 n = input()\
n = int(n)\
r = \cf4 \cb1 \strokec4 0\cf2 \cb3 \strokec2 \
mat = [\cf4 \cb1 \strokec4 1\cf2 \cb3 \strokec2 ] * n\
\pard\pardeftab720\sl220\partightenfactor0

\f1\b \cf5 \cb1 \strokec5 for
\f0\b0 \cf2 \cb3 \strokec2  i 
\f1\b \cf5 \cb1 \strokec5 in
\f0\b0 \cf2 \cb3 \strokec2  range(n):\
    st = input()\
    front, back = (int(a) 
\f1\b \cf5 \cb1 \strokec5 for
\f0\b0 \cf2 \cb3 \strokec2  a 
\f1\b \cf5 \cb1 \strokec5 in
\f0\b0 \cf2 \cb3 \strokec2  st.split())\
    
\f1\b \cf5 \cb1 \strokec5 if
\f0\b0 \cf2 \cb3 \strokec2  min(front, back) >= \cf4 \cb1 \strokec4 0\cf2 \cb3 \strokec2  
\f1\b \cf5 \cb1 \strokec5 and
\f0\b0 \cf2 \cb3 \strokec2  front + back == n - \cf4 \cb1 \strokec4 1\cf2 \cb3 \strokec2 :\
        
\f1\b \cf5 \cb1 \strokec5 if
\f0\b0 \cf2 \cb3 \strokec2  front < n 
\f1\b \cf5 \cb1 \strokec5 and
\f0\b0 \cf2 \cb3 \strokec2  mat[front] != \cf4 \cb1 \strokec4 2\cf2 \cb3 \strokec2 :\
            mat[front] = \cf4 \cb1 \strokec4 2\cf2 \cb3 \strokec2 \
            r += \cf4 \cb1 \strokec4 1\cf2 \cb3 \strokec2 \
print(r)}