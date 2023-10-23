dataFrame = pd.DataFrame({"TotalPopulation": TotalPopulation,
                     "FemalePopulation": FemalePopulation,
                     "MalePopulation": MalePopulation,
                     "BirthRate": BirthRate,
                     "DeathRate": DeathRate,
                     "MaleExpectancy": MaleExpectancy,
                     "FemaleExpectancy":FemaleExpectancy,
                     "PriEnroll":PriEnroll,
                     "TerEnroll":TerEnroll,
                     "PriComple":PriComple,
                     "LiterRate":LiterRate,
                     "Country": tempCountry,
                     "Year": tempYear
                     },index = None)
    return dataFrame