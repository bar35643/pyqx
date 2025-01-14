#!/usr/bin/env python
#coding: utf-8

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
import numpy as np
import sys

arr = np.empty(0)
img0 = None


class Image:

    def __init__(self, fileName, image, bg, context):

        self.fileName = fileName
        self.image = image
        self.bgColor = bg
        self.context = context

        self.zoom = 1
        self.selection = None
        self.history = [QtGui.QImage(self.image)]
        self.posHistory = 0
        self.modified = False

    @classmethod
    def fromFile(cls, fileName, context):

        image = QtGui.QImage(fileName[0]).convertToFormat(
            QtGui.QImage.Format_ARGB32_Premultiplied)
        """
        global img0
        img0 = QtGui.QImage(fileName[0]).convertToFormat(
            QtGui.QImage.Format_ARGB32_Premultiplied)

        # Create Numpy Array
        np.set_printoptions(threshold=sys.maxsize)
        incomingImage = image.convertToFormat(QtGui.QImage.Format.Format_RGB32)
        width = incomingImage.width()
        height = incomingImage.height()
        ptr = incomingImage.bits()
        ptr.setsize(height * width * 4)
        global arr
        arr = np.frombuffer(ptr, np.uint8).reshape((height, width, 4))
        """
        if image.hasAlphaChannel():
            bgColor = QtGui.QColor(0, 0, 0, 0)
        else:
            bgColor = QtGui.QColor(255, 255, 255)

        return cls(fileName, image, bgColor, context)

    @classmethod
    def newImage(cls, w, h, bg, context):

        image = QtGui.QImage(w, h, QtGui.QImage.Format_ARGB32_Premultiplied)
        image.fill(bg)

        return cls("", image, bg, context)

    def save(self):
        """
        # Create Numpy Array
        np.set_printoptions(threshold=sys.maxsize)
        incomingImage = self.image.convertToFormat(
            QtGui.QImage.Format.Format_RGB32)
        width = incomingImage.width()
        height = incomingImage.height()
        ptr = incomingImage.bits()
        ptr.setsize(height * width * 4)
        arr1 = np.frombuffer(ptr, np.uint8).reshape((height, width, 4))
        global arr
        diff = np.abs(arr1 - arr)
        qim = QtGui.QImage(
            diff.data, diff.shape[1], diff.shape[0], diff.strides[0], QtGui.QImage.Format.Format_RGB32)

        print(self.fileName[0].split("."))
        global img0
        img0.save(self.fileName[0].split(".")[0] + "_original" + ".png")
        self.image.save(self.fileName[0].split(".")[0] + "_new" + ".png")
        qim.save(self.fileName[0].split(".")[0] + "_diff" + ".png")
        """
        self.image.save(self.fileName[0])
        self.modified = False

    def addHistoryStep(self):

        if self.posHistory != len(self.history) - 1:
            self.history = self.history[:self.posHistory + 1]
        self.history.append(QtGui.QImage(self.image))

        self.posHistory += 1
        self.modified = True

    def paintPoint(self, x, y, color, size):

        painter = QtGui.QPainter(self.image)
        painter.setPen(color)
        painter.setCompositionMode(QtGui.QPainter.CompositionMode_Source)
        painter.drawPixmap(QtCore.QPoint(x - size + 1, y -
                           size + 1), self.context.brushes[size - 1])

    def createMaskFromArea(self, point, threshold=0):

        mask = self.recursiveFill(QtGui.QImage(
            self.image), point, self.image.pixel(point))
        return mask

    """
	def recursiveFill(self, mask, point, threshold=0, color=None):

		x, y = point.x(), point.y()

		# The recursive algorithm. Starting at x and y, changes any adjacent
		# characters that match oldChar to newChar.
		width = mask.width()
		height = mask.height()

		if color == None:
			color = mask.pixel(x,y)

		if mask.pixel(x,y) != color:
			# Base case. If the current x, y character is not the oldChar,
			# then do nothing.
			return

		# Change the character at world[x][y] to newChar
		mask.setPixel(x, y, QtCore.Qt.color0)

		# Recursive calls. Make a recursive call as long as we are not on the
		# boundary (which would cause an Index Error.)
		if x > 0: # left
			self.recursiveFill(mask, QtCore.QPoint(x-1, y))

		if y > 0: # up
			self.recursiveFill(mask, QtCore.QPoint(x, y-1))

		if x < width-1: # right
			self.recursiveFill(mask, QtCore.QPoint(x+1, y))

		if y < height-1: # down
			self.recursiveFill(mask, QtCore.QPoint(x, y+1))
	"""

    def recursiveFill(self, mask, point, color, threshold=0):

        x, y = point.x(), point.y()

        if x < 0 or y < 0 or x > mask.width() - 1 or y > mask.height() - 1:
            return

        elif mask.pixel(x, y) == color:
            mask.setPixel(x, y, QtCore.Qt.color0)
            self.recursiveFill(mask, QtCore.QPoint(x + 1, y), color)
            self.recursiveFill(mask, QtCore.QPoint(x, y + 1), color)
            self.recursiveFill(mask, QtCore.QPoint(x - 1, y), color)
            self.recursiveFill(mask, QtCore.QPoint(x, y - 1), color)
