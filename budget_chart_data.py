def get_chart_data(categories, totalWthdrawn):
    percentSpentDictionary = {
        100 : [],
        90 : [],
        80 : [],
        70 : [],
        60 : [],
        50 : [],
        40 : [],
        30 : [],
        20 : [],
        10 : [],
        0 : [],
    }
    
    
    for category in categories:        
        totalSpentPerCategory = sum(category.withdraws)
        
        percentageSpent = (totalSpentPerCategory / totalWthdrawn) * 100
        #Round to nearest 10
        roundedPercentSpend = int(percentageSpent - (percentageSpent % 10))
        
        for key in percentSpentDictionary:
            if roundedPercentSpend >= key:
                percentSpentDictionary[key].append("o")
            else:
                percentSpentDictionary[key].append(" ")
                
    return percentSpentDictionary

                    
                    
def get_spend_chart_labels(categories):
    #Spaces are for formatting to match expected output
    labels ="     "
    categoryNames = [category.category for category in categories]
    count = len(max(categoryNames, key = len))
    
    for i in range(count):
        for category in categories:
            if len(category.category) > i:
                labels += category.category[i] + "  "
            else:
                labels += "   "
                
        if i != count - 1:
            labels += "\n     "
            
    return labels