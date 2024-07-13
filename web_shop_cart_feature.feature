Feature: Cart functionality
  User want to use all cart functions correctly

  Scenario: Check whether user can see the cart badge get updated when add items to cart
     Given User enters visual user Username and Password
     When User clicks add to cart button
     Then User should see the updated cart icon

  Scenario: Check whether user can see the cart items added to cart
     Given User enters visual user Username and Password
     When User clicks add to cart button
     Then User finds the cart items added to cart

  Scenario: Check whether user can go to checkout from cart
     Given User enters visual user Username and Password
     When User clicks add to cart button
     Then User is now checked out