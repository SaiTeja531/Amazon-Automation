# Amazon-Automation
## Framework for selenium automation on amazon.in using POM and pytest unit testing framework  
### PageObjects-Folder contains 
  1.LoginPage.py-->Where the Login page elements and required objects for login page is present  
  2.HomePage.py--> where the homepage elements and required objects for home page are present
#### Iam further trying to develop this project by keeping all the elements inside a test data folder  
### Utilities -Folder contains
  1.Base.py-->This is a super class for all the classes present in this project it contains most frequently used methods inside every python file in 
     this project      
  2.fixture.py-->This python file contains all the fixtures used in this project we will inherit this class and use the fixtures we need inside a test case  
#### I will further add more fixtures and common utilites in the Utilities folder  
### Test cases-Folder contains  
  1.conftest.py-->this is a setup and teardown fixture which contains a common fixture of opening the browser and initiating the driver and closing the browser  
  2.test_case001.py-->This test case checks the login functionality  
  3.test_case002.py-->This test case checks the navigation bar of amazon page like  
      -->search box enters a text and prints the suggestions  
      -->checks the flag is displayed and prints the languages present  
      -->checks the user is displayed correctly according to the login and prints all the buttons inside the hover menu  
      -->customer since text is displayed or not and prints it 
      -->movie recommendation is displayed or not and prints it  
  4.test_case003.py-->This test case checks the 'all' button on amazon page clicks on the best sellers and goes to the page and prints the title  
  #### Iam trying to make the 'test-case003.py' more generic by going to the user clicked page and coming back to the home page and again clicking on another button
   
