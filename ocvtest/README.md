# ocvtest

This is implemented examples of OpenCV-Python Tutorials.

#### Links:
* [OpenCV 3.0.0 tutorial](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html)
* [OpenCV 3.3.1 tutorial](https://docs.opencv.org/3.3.1/d6/d00/tutorial_py_root.html)

## Notes

**Low-pass filters** (LPF) helps in removing noises, blurring the images etc.

**High-pass filters** (HPF) helps in finding edges in the images.

### Structuring Element (Kernel shape)

[Link: docs - structuring-element](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html#structuring-element)

[Morphological Operations at HIPR2](http://homepages.inf.ed.ac.uk/rbf/HIPR2/morops.htm)

We manually created a structuring elements in the previous examples with help of Numpy.
It is rectangular shape. But in some cases, you may need elliptical/circular shaped kernels.
So for this purpose, OpenCV has a function, `cv2.getStructuringElement()`.
You just pass the shape and size of the kernel, you get the desired kernel.

```
# Rectangular Kernel
>>> cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]], dtype=uint8)

```
```
# Elliptical Kernel
>>> cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
array([[0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0]], dtype=uint8)
```
```
# Cross-shaped Kernel
>>> cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
array([[0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0]], dtype=uint8)
```