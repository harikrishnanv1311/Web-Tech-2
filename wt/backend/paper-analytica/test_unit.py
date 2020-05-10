from flask import Flask
import unittest 
from app import app 

class AppUnitTesting(unittest.TestCase): 
  def setUp(self):
    # app.config['TESTING'] = True
    # app.config['WTF_CSRF_ENABLED'] = False
    # app.config['DEBUG'] = False
    self.app = app.test_client()
    self.app.testing = True 
    # print(app)
  
  def tearDown(self):
        pass 
  
  def testNormalCase1(self): 
      print()
      print("************************************************************************")
      print("*************************  Normal Test Case 1  *************************")
      print("************************************************************************")
      print()   
      response = self.app.get('getRecommendation/neural')
      #print("The Response is:",response.data)
      self.assertIsNotNone(response.data) 
  
  def testNormalCase2(self):
      print()
      print("************************************************************************")
      print("*************************  Normal Test Case 2  *************************")
      print("************************************************************************")
      print()     
      response = self.app.get('getRecommendation/clustering')
      #print("The Response is:",response.data)
      self.assertIsNotNone(response.data)
  
  def testNormalCase3(self): 
      print()
      print("************************************************************************")
      print("*************************  Normal Test Case 3  *************************")
      print("************************************************************************")
      print()  
      response = self.app.get('getRecommendation/processing')
      #print("The Response is:",response.data)
      self.assertIsNotNone(response.data)

  def testNormalCase4(self):
      print()
      print("************************************************************************")
      print("*************************  Normal Test Case 4  *************************")
      print("************************************************************************")
      print()   
      response = self.app.get('getRecommendation/system')
      #print("The Response is:",response.data)
      self.assertIsNotNone(response.data)

  def testNormalCase5(self):  
      print()
      print("************************************************************************")
      print("*************************  Normal Test Case 5  *************************")
      print("************************************************************************")
      print() 
      response = self.app.get('getRecommendation/convergence')
      #print("The Response is:",response.data)
      self.assertIsNotNone(response.data)
  
  #Sending 1 whitespace
  def testExceptionalCase1(self):
      print()
      print("*****************************************************************************")
      print("*************************  Exceptional Test Case 1  *************************")
      print("*****************************************************************************")
      print()   
      response = self.app.get('getRecommendation/ ')
      #print("The Response is:",response.data)
      self.assertIsNotNone(response.data)
  
  #Sending 3 whitespace
  def testExceptionalCase2(self):
      print()
      print("*****************************************************************************")
      print("*************************  Exceptional Test Case 2  *************************")
      print("*****************************************************************************")
      print()
      response = self.app.get('getRecommendation/   ')
      #print("The Response is:",response.data)
      self.assertIsNotNone(response.data)

  #Sending with tabs
  def testExceptionalCase3(self):
      print()  
      print("*****************************************************************************")
      print("*************************  Exceptional Test Case 3  *************************")
      print("*****************************************************************************")
      print() 
      response = self.app.get('getRecommendation/         ')
      #print("The Response is:",response.data)
      self.assertIsNotNone(response.data)

  #Sending with only numbers
  def testExceptionalCase4(self): 
      print()
      print("*****************************************************************************")
      print("*************************  Exceptional Test Case 4  *************************")
      print("*****************************************************************************")
      print()  
      response = self.app.get('getRecommendation/123')
      #print("The Response is:",response.data)
      self.assertIsNotNone(response.data)
    
  #Sending with alphanumerics
  def testExceptionalCase5(self):
      print()
      print("*****************************************************************************")
      print("*************************  Exceptional Test Case 5  *************************")
      print("*****************************************************************************")
      print()   
      response = self.app.get('getRecommendation/compu155ter')
      #print("The Response is:",response.data)
      self.assertIsNotNone(response.data)
  
  #Sending with only special characters
  def testExceptionalCase6(self): 
      print()
      print("*****************************************************************************")
      print("*************************  Exceptional Test Case 6  *************************")
      print("*****************************************************************************")
      print()  
      response = self.app.get('getRecommendation/!^#%$')
      #print("The Response is:",response.data)
      self.assertIsNotNone(response.data)
    
  #Sending with alphabets and special characters
  def testExceptionalCase7(self): 
      print()
      print("*****************************************************************************")
      print("*************************  Exceptional Test Case 7  *************************")
      print("*****************************************************************************")
      print()  
      response = self.app.get('getRecommendation/net{}work')
      #print("The Response is:",response.data)
      self.assertIsNotNone(response.data)
    
  #Sending with alphanumerics and special characters
  def testExceptionalCase8(self):
      print()
      print("*****************************************************************************")
      print("*************************  Exceptional Test Case 8  *************************")
      print("*****************************************************************************")
      print()   
      response = self.app.get('getRecommendation/optimi$ati0n')
      #print("The Response is:",response.data)
      self.assertIsNotNone(response.data)

  '''FOR STAT RETRIEVAL, CHECK IS DONE IN THE ABOVE API's WHICH ARE USED 
  TO GENERATE THE APPROPRIATE STATISTIC'''
  def testStatYearHistogram1(self):
      print()
      print("********************************************************************************")
      print("*************************  Year Histogram Test Case 1  *************************")
      print("********************************************************************************")
      print()
        
      response = self.app.get('getRecommendation/network')
      image = self.app.get('/getHistogram/year')
      #print("The Response is:",response.data)
       
      self.assertIsNotNone(response.data)
      self.assertIsNotNone(image.data)
      print()
      # print("The below warning is for not closing a file and can be ignored!")
      

  def testStatYearHistogram2(self):
      print()
      print("******************************************************************************************")
      print("*************************  Year Histogram Exception Test Case 1  *************************")
      print("******************************************************************************************")
      print()
        
      response = self.app.get('getRecommendation/n3tw0r!<')
      image = self.app.get('/getHistogram/year')
      #print("The Response is:",response.data)
      
      self.assertIsNotNone(response.data)
      self.assertIsNotNone(image.data)
      print()
      # print("The below warning is for not closing a file and can be ignored!")
      

  def testStatAuthorHistogram1(self):
      print()
      print("**********************************************************************************")
      print("*************************  Author Histogram Test Case 1  *************************")
      print("**********************************************************************************")
      print()   
      response = self.app.get('getRecommendation/network')
      image = self.app.get('/getHistogram/author')
      #print("The Response is:",response.data)
      self.assertIsNotNone(response.data)
      self.assertIsNotNone(image.data)
      print()
      # print("The below warning is for not closing a file and can be ignored!")

  def testStatAuthorHistogram2(self):
      print()
      print("********************************************************************************************")
      print("*************************  Author Histogram Exception Test Case 1  *************************")
      print("********************************************************************************************")
      print()
        
      response = self.app.get('getRecommendation/n3tw0r!<')
      image = self.app.get('/getHistogram/author')
      #print("The Response is:",response.data)
      
      self.assertIsNotNone(response.data)
      self.assertIsNotNone(image.data)
      print()
      # print("The below warning is for not closing a file and can be ignored!")

if __name__ == '__main__':  
    unittest.main() 