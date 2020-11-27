# Irrational numbers

The decimal representation that has been introduced in the last exercise is one way of representing the real numbers.  Decimals are not the only way that the real numbers can be represented, however.  In the same way that you have seen for the natural numbers, there are multiple of representing the real numbers.  You will come to understand during your math degree that we need these alternative representations in order to better understand the underlying objects and to not get distracted by the shadows that are cast when real numbers are represented as decimals. 

We can represent some of the real numbers as fractions.  As we have seen in the previous tasks, the numbers that can be represented in this way are the so-called rational numbers.  Consider the following derivation, however:

![](https://render.githubusercontent.com/render/math?math=\sqrt{2}=1%2B(\sqrt{2}-1)=1%2B\frac{(\sqrt{2}-1)(\sqrt{2}%2B1)}{\sqrt{2}%2B1}=1%2B\frac{2-1}{\sqrt{2}%2B1}=1%2B\frac{1}{1%2B\sqrt{2}})

The point I am trying to make above is that despite our best efforts, we cannot extract an expression for the square root of 2, which has the square root of two on the left-hand side and a quotient on the right-hand side.  The best we can do is we can replace the square root of 2 on the right-hand side here with the expression on the right-hand side as follows:

![](https://render.githubusercontent.com/render/math?math=\sqrt{2}=1%2B\frac{1}{2%2B\frac{1}{1%2B\sqrt{2}}})

There is still a square root on the right-hand side, however, which we could replace with the right-hand side once more to obtain:

![](https://render.githubusercontent.com/render/math?math=\sqrt{2}=1+\frac{1}{2%2B\frac{1}{1%2B\frac{1}{2%2B\frac{1}{1%2B\sqrt{2}}}})

Hopefully, it is clear that the number of times we perform the operation above does not matter.  The expression will always contain a square root of two on the right-hand side.  To find an exact value for root 2 we thus have to imagine that this operation is done an infinite number of times.

The point that I am trying to make here is that an infinite number of mathematical operations are required to obtain representations of the so-called irrational numbers.  These irrational numbers are defined as follows:

_A number x is called irrational if it cannot be written as the quotient of two non-zero integers._

Let me be clear here, the existence of such numbers should hurt your brain!  A lot of your first year will be spent thinking about why these irrational numbers exist and in learning mathematical tools for handling them.  If these tools are to be useful to you it worth investing time to identify the ways in which real numbers (and the decimal representation of them in particular) do not follow your common-sense notions about numbers.  If you do spend this time thinking about why these numbers are weird you will be able to better understand why the tools you are being taught have been developed.

A first odd thing for you to understand is that irrational numbers cannot be represented in binary.  In programs that use irrational numbers, we thus have to use approximations of these numbers or we have to use symbolic computation.  In this task, you are going to try to write code calculate an approximate value of the square root of two using the maths described above.  I have started off by assuming that the square root of two is one and by inserted into this expression:

![](https://render.githubusercontent.com/render/math?math=\sqrt{2}=1%2B\frac{1}{1%2B\sqrt{2}})

This has been done in the line:

````
est = 1 + 1 / 2
````

The variable `est` is (based on the expression above) a better estimate for the square root of two.  Furthermore, if you insert this estimate into the expression above again you should get an even better estimate for the value of the square root of two.  To complete the task I would thus like you to write a loop that generates these progressively better and better estimates for the value of the square root of two.  Your progressively better and better estimates for the value of the square root of two should be stored in the numpy array called `yvals`.  If you complete the exercise correctly a graph showing how the value of this estimate changes as the number of times the estimate is inserted into the expression above should appear. 

------

## IMPORTANT NOTE: 

The mathematics outlined here __DOES NOT__ prove that the square root of two is irrational.  What has been presented is just an interesting observation about the square root of 2. 
