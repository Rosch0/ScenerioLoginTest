Feature: Login button activation

Login button should be inactive, when fields are not filled or filled unproperly.

Scenario: Unactive Log in button on empty fields
	Given I am on the login page 1
	When I kill cookies
	And The 'Email' and 'Password' field is empty
	Then Log in button should be in disabled state 1

Scenario: Log in button state - bad Email syntax
	Given I am on the login page 2
	When I kill cookies 2
	And I type 'Bad Syntax Email' in Email Field
	And I type 'Registed User Pwd' in Passowrd Field 1
	Then Log in button should be in disabled state 2

Scenario: Log in button state - good Email syntax
	Given I am on the login page 3
	When I kill cookies 3
	And I type 'Good Syntax Email' in Email Field
	And I type 'Registed User Pwd' in Passowrd Field 2
	Then Log in button should be in active state