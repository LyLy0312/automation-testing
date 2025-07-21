Feature: Filter stocks by industry

  Scenario Outline: User filters stocks by one or more industries and views result
    Given the user is logged in
    When the user selects industries <industries>
    And the user clicks the Filter button
    Then the result list should contain stocks in <industries>

    Examples:
      | industries                       |
      | ["Ngân hàng"]                    |
      | ["Bảo hiểm"]                     |
      | ["Ngân hàng", "Bảo hiểm"]        |
      | ["Bán lẻ", "Dược phẩm và Y tế"]  |
