# Process Calculator

This library is meant to provide efficient analysis of business processes including:

- Finding the break even point of different processes using its fixed and variable costs.
- To be determined.
- To be determined.

## BreakEven

Primary class to find the break even point between two processes. This class omits getter methods but allows the use of properties. Setter methods are included and multiple ways of constructing the object are also available.

### Constructor method

The constructor method has its default variables set to 0 in the case of `fixed1` and `fixed2` and `[0]` in the case of `variable1` and `variable2`.

Example of default construction:

```{python}
    # Create blank breakEven object
    import processCalculator
    be = processCalculator.breakEven.breakEven()
```

The default values of the object can be changed by changing the constructor arguments. Fixed cost arguments are `float` data types while `variable` cost arguments can be either of type `float` or type `list`.

Example of custom construction:

```{python}
    #Create custom breakEven object
    import processCalculator
    #Single value variable costs
    be = processCalculator.breakEven.breakEven(
        fixed1    = 22.34 #represents process 1 having a fixed cost of 22.34
        variable1 = 2.30  #represents process 1 having a variable cost of 2.30
        fixed2    = 25.20 #represents process 2 having a variable cost of 25.20
        variable2 = 1.30  #represents process 2 having a variable cost of 1.30
    )
    #Multiple value variable costs
    be2 = processCalculator.breakEven.breakEven(
        fixed1    = 22.34 #represents process 1 having a fixed cost of 22.34
        variable1 = [2.30, 1.20]  #represents process 1 having multiple variable costs
        fixed2    = 25.20 #represents process 2 having a variable cost of 25.20
        variable2 = [1.30, 3.20]  #represents process 2 having multiple variable costs
    )
```

### Setter methods

Setter methods follow a the *setVariableName* syntax.

Example of setter methods:

```{python}
    # Create breakEven object
    be = processCalculator.breakEven.breakEven()
    #Set fixed and variable costs
    be.setFixed1(22.34)
    be.setVariable1([1.30, 1.20])
    be.setFixed2(20.20)
    be.setVariable2([2.20, 0.50])
```
