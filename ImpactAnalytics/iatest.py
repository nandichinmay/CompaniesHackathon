# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 13:20:00 2021

@author: nandi
"""



class RectangleOutline:
    
    def rectangleDip(self, rectangle):
        noOfRectangle = len(rectangle)
        if noOfRectangle == 0: # 0 rectangle cardboard
            return []
        if noOfRectangle == 1: # 1 rectangle cardboard
            x_start, x_end, y = rectangle[0]
            return [(x_start, y), (x_end, 0)] 
        # more than 1 rectangle cardboard
        leftRectangleCord = self.rectangleDip(rectangle[: noOfRectangle // 2])
        rightRectangleCord = self.rectangleDip(rectangle[noOfRectangle // 2 :])
        return self.mergeRectangleCord(leftRectangleCord, rightRectangleCord)
    
    
    
    def mergeRectangleCord(self, leftRectangleCord, rightRectangleCord):
       
        def updateResult(x, y):
            if not result or result[-1][0] != x:
                result.append((x, y))
            else:
                result[-1][1] = y
        
        def appendRectangleCord(index, remainingCord, total, y, currYCord): 
            while index < total: 
                x, y = remainingCord[index]
                index += 1
                if currYCord != y:
                    updateResult(x, y)
                    currYCord = y
         
            
            
        noOfLeftRectangleCord, noOfRightRectangleCord= len(leftRectangleCord), len(rightRectangleCord)
        leftIndex = 0 
        rightIndex = 0
        
        currYCord  = 0
        leftYCord= 0
        rightYCord= 0
        
        result = []
            
        while leftIndex < noOfLeftRectangleCord and rightIndex < noOfRightRectangleCord:
            leftCord, rightCord = leftRectangleCord[leftIndex], rightRectangleCord[rightIndex]
            
            if leftCord[0] < rightCord[0]: 
                x, leftYCord = leftCord
                leftIndex += 1
            else: 
                x, rightYCord = rightCord 
                rightIndex += 1
                
            maxYCord = max(leftYCord, rightYCord)
            if currYCord != maxYCord:
                updateResult(x, maxYCord)
                currYCord = maxYCord

        appendRectangleCord(leftIndex, leftRectangleCord, noOfLeftRectangleCord, leftYCord, currYCord) #remaining left side

        appendRectangleCord(rightIndex, rightRectangleCord, noOfRightRectangleCord, rightYCord, currYCord) #remaining right side
                
        return result
    
rectangleOutline=RectangleOutline()

inputStr = input("Please enter your data")
inputList=eval(inputStr)
print(rectangleOutline.rectangleDip(inputList))
