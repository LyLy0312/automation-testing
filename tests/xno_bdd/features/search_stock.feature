Feature: Search for a stock

  Scenario Outline: Search for a stock and verify result
    Given the user is logged in
    When the user searches for "<stock_code>"
    Then the stock "<stock_code>" should be in the result list

    Examples:
      | stock_code |
      | SSI        |
      | FPT        |
      | VNM        |
