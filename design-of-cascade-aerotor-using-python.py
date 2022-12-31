from fpdf import FPDF
import os
def main():
    def start ():
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("                                    Design of Cascade Aerator")
        print("-----------------------------------------------------------------------------------------------------------------------")
        print("1. Start Design")
        print("2. Change/View Assumptions")
        print("3. Exit")   
        print("-----------------------------------------------------------------------------------------------------------------------")
    start()
    def choiceMainMenu():
        choiceMainMenu.choice=int(input("Enter Your Choice : "))
        if choiceMainMenu.choice==1:
            os.system('cls')
            print("-----------------------------------------------------------------------------------------------------------------------")
            print(" - Design Section")
            print("-----------------------------------------------------------------------------------------------------------------------")
            def data():
                data.surfaceLoadingRate=0.04 #m^2/m^3/hr IT HAS RANGE (0.02 - 0.05)
                data.velocityOfCentralPipe=1 #1 m/s
                data.velocityThroughChannel=1 #1 m/s
                data.velocityOfWaterThroughTheCascade=1 #1 m/s
                data.pi=3.14 #for calculation area of circle
                data.thicknessOfCentralShaft=0.3 #0.3m
                data.numberOfSteps=10 #10 steps
                data.widthToDepth=1 #Width to depth ratio
                data.width=1 #from width to depth ratio
                data.depth=1 #from widht to depth ratio
                data.freeBoardToLaunder=0.4 #Free board provided to launder is 0.4
                data.heightOfAerator=5 #Assume the height of aerator is 5m
                data.numberOfRisers=11 #No. Riser to be provided is 11
                data.heightOfEachRiser=(data.heightOfAerator/data.numberOfRisers)
            data()

            def discharge():
                discharge.inputDischargeInMLD=int(input("Enter the Rate of Flow (MLD) : - "))
                discharge.flowRate=((discharge.inputDischargeInMLD*10**3)/24)
                discharge.discharge=discharge.flowRate/(60*60)
                print("Flow Rate = " + str(round(discharge.flowRate, 3)) + " m^3/hr")
                print("Q = " + str(round(discharge.discharge, 3)) + " m^3/s")
            discharge()

            def areaOfCascade():
                areaOfCascade.areaOfCascadeAerator=data.surfaceLoadingRate * discharge.flowRate
                print("Area of Cascade Aerator = " + str(round(areaOfCascade.areaOfCascadeAerator, 3)) + " m^2")
                #areaOfCascade.diameterOfCascadeAerator=(areaOfCascade.areaOfCascadeAerator/(data.pi/4))**(1/2)
                #print("Diameter of Cascade = " +str(round(areaOfCascade.diameterOfCascadeAerator, 3)) + " m")
            areaOfCascade()

            def calOfCentralPipeAndShaft():
                calOfCentralPipeAndShaft.areaOfCentralPipe=(discharge.discharge)/(data.velocityOfCentralPipe)
                print("Area of Central Pipe = " + str(round(calOfCentralPipeAndShaft.areaOfCentralPipe, 3)) +" m^2")
                calOfCentralPipeAndShaft.diameterOfCentralPipe=((calOfCentralPipeAndShaft.areaOfCentralPipe)/(data.pi/4))**(1/2)
                print("Diameter of Central Pipe = " + str(round(calOfCentralPipeAndShaft.diameterOfCentralPipe, 1)) + " m")
                calOfCentralPipeAndShaft.diameterOfCentralShaft=calOfCentralPipeAndShaft.diameterOfCentralPipe + (data.thicknessOfCentralShaft*2)
                print("Diameter of Central Shaft = " + str(round(calOfCentralPipeAndShaft.diameterOfCentralShaft, 1)) + " m") 
                calOfCentralPipeAndShaft.areaofCentralShaft=(((data.pi)/(4))*((calOfCentralPipeAndShaft.diameterOfCentralShaft)**(2)))
                print("Area of Central Shaft = " + str(round(calOfCentralPipeAndShaft.areaofCentralShaft, 2)) + " m^2")
            calOfCentralPipeAndShaft()

            def calOfCascade():
                calOfCascade.totalAreaOfCascade=(areaOfCascade.areaOfCascadeAerator + calOfCentralPipeAndShaft.areaofCentralShaft)
                print("Total Area of Cascade = " + str(round(calOfCascade.totalAreaOfCascade,2)) + " m^2")
                calOfCascade.diameterOfTotalCascade=((calOfCascade.totalAreaOfCascade)/(data.pi/4))**(1/2)
                print("Diameter of Cascade Aerator = " + str(round(calOfCascade.diameterOfTotalCascade, 2)) + " m")
                #Setps in Cascade Aerator
                calOfCascade.d=[]
                n=2
                for i in range(0, data.numberOfSteps):
                    valD=(n)*3.51
                    n+=1
                    valD1=round(valD, 2)
                    calOfCascade.d.append(valD1)
                print("Diameter of Cascade 1st to " + str(data.numberOfSteps) + " th")
                print(calOfCascade.d)
                print(calOfCascade.d[data.numberOfSteps-1])
                print("Diameter of Cascade Aerator = " + str(round(calOfCascade.diameterOfTotalCascade, 2)) + " m " + "=" " Diameter of Bottom Cascade = " + str(round((calOfCascade.d[data.numberOfSteps-1]))) + " m")
                checkDifference=(round((calOfCascade.d[data.numberOfSteps-1]))) - (round(calOfCascade.diameterOfTotalCascade, 2))
                if checkDifference > 0.30:
                    print("#Condition/Check not Satisfied")
                elif checkDifference < 0.30:
                    print("#Contidion/Check Satisfied")
                else:
                    print("Error !")
                calOfCascade.lengthOfEachTrade=((calOfCascade.d[data.numberOfSteps-1])/2)/11
            calOfCascade()

            def dimensionOfAerator():
                dimensionOfAerator.diameterOfTip=(calOfCascade.diameterOfTotalCascade/data.numberOfRisers)
                print("Diameter of Tip = " + str(round(dimensionOfAerator.diameterOfTip,2)) + " m")
                print("Check, Diameter of tip > Diameter of Central Pipe")
                if dimensionOfAerator.diameterOfTip > calOfCentralPipeAndShaft.diameterOfCentralPipe:
                    print("Condition/Check Satisfied")
                else:
                    print("Error !")
            dimensionOfAerator()

            def calOfLaunder():
                calOfLaunder.flowRateValue=((round(discharge.discharge, 3))/2)
                print("The Flow Rate Value = " + str(round(calOfLaunder.flowRateValue, 3)) + " m^3/s")
                calOfLaunder.area=(calOfLaunder.flowRateValue)/(data.velocityThroughChannel)
                print("Area of Launder = " +str(round(calOfLaunder.area, 3)) + " m")
                calOfLaunder.width=calOfLaunder.area/(data.depth+data.depth)
                calOfLaunder.depthWithoutLaunder=calOfLaunder.area/(data.width+data.width)
                calOfLaunder.depth=round((calOfLaunder.depthWithoutLaunder+data.freeBoardToLaunder),3)
                print("Width of Launder = " + str(round(calOfLaunder.width, 3)) + " m")
                print("Depth of Launder = " + str(round(calOfLaunder.depth, 3)) + " m")
            calOfLaunder()

            def finalOutput():
                print("-----------------------------------------------------------------------------------------------------------------------")
                print("Design Summary")
                print("-----------------------------------------------------------------------------------------------------------------------")
                print("1. Area of Cascade : " + str(round(areaOfCascade.areaOfCascadeAerator, 3)) + " m^2")
                print("2. Diameter of Central Pipe : " + str(round(calOfCentralPipeAndShaft.diameterOfCentralPipe, 1)) + " m")
                print("3. Diameter of Central Shaft : " + str(round(calOfCentralPipeAndShaft.diameterOfCentralShaft, 1)) + " m") 
                print("4. Diameter of total cascade aerator : " + str(round(calOfCascade.diameterOfTotalCascade, 0)) + " m")
                print("5. Flow Rate Value : " + str(round(calOfLaunder.flowRateValue, 3)) + " m^3/s")
                print("6. Width of Launder : " + str(round(calOfLaunder.width, 3)) + " m")
                print("7. Depth of Launder : " + str(round(calOfLaunder.depth, 3)) + " m")
                print("8. Velocity of Water Through the cascade : " + str(data.velocityOfWaterThroughTheCascade) + " m")
                print("9. Rise of Cascade : " + str(round(data.heightOfEachRiser, 2)) + " m")
                print("10. Trade of Cascade : "+ str(round(calOfCascade.lengthOfEachTrade, 2))+ " m")
                print("11. Number of Steps provided in cascade : " + str(round(data.numberOfRisers)) + " Nos")
                print("12. Height of Aerator is : "+str(data.heightOfAerator) + " m" )
            finalOutput()
            def finalPrintToPDF():
                pdf = FPDF() #Making a PDF Variable
                pdf.add_page() #Adding a Page
                pdf.set_font("Arial" , size= 15) #Font ani Size
                #Actual Printing in PDF Starts here...........
                pdf.cell(200, 10, txt = "Design Of Cascade Aerator",
                    ln = 1, align = 'C')
                pdf.cell(200, 10, txt = "(" +str(round(discharge.inputDischargeInMLD, 0))+ " MLD" ")",
                    ln = 2, align = 'C')
                pdf.cell(200, 10, txt = "GIVEN : - ",
                    ln = 3, align = 'L')    
                pdf.cell(200,10, txt = "          Q = " +str(discharge.inputDischargeInMLD) + " MLD",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "              = " +str((discharge.inputDischargeInMLD)*10**6) + " l/d",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "              = " +str((discharge.inputDischargeInMLD)*(10**6)*(10**-3)) + " m^3/d",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "              = " +str(round((((discharge.inputDischargeInMLD)*10**3)/24), 3)) + " m^3/hr",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "              = " +str((((discharge.inputDischargeInMLD)*10**3)/24)/(60*60)) + " m^3/s",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "             ",
                    ln = 4, align = 'L')
                pdf.cell(200, 10, txt = "Step 1 : Determination of Aera of Cascade Aerator - ",
                    ln = 3, align = 'L')
                pdf.cell(200,10, txt = "          Surface Loading Rate = " +str(data.surfaceLoadingRate) + " m^2/m^3/hrs",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Flow Rate = " +str(round((((discharge.inputDischargeInMLD)*10**3)/24), 3)) + " m^3/hr",
                    ln = 4, align = 'L')   
                pdf.cell(200,10, txt = "          Area of Cascade Aerator = Surface Loading Rate x Flow Rate",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Area of Cascade Aerator = " +str(round(areaOfCascade.areaOfCascadeAerator, 2)) + " m^2",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "             ",
                    ln = 4, align = 'L')
                pdf.cell(200, 10, txt = "Step 2 : Calculation For The Diameter of Central Pipe and Shaft - ",
                    ln = 3, align = 'L')
                pdf.cell(200,10, txt = "          Assume the Velocity of Central Pipe = " +str(data.velocityOfCentralPipe) + " m/s",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          By continuity equation, ",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Q = A x V ",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          A = Q x V ",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          A = " +str(round((discharge.inputDischargeInMLD/data.velocityOfCentralPipe),3)) + " m^2",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          A = (pi/4) x Diameter of Central Pipe ",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Diameter of Central Pipe = " +str(round(calOfCentralPipeAndShaft.diameterOfCentralPipe, 1)) + " m",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Now, Assume the thickness of Central Shaft = " +str(data.thicknessOfCentralShaft) + " m",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Outer Diameter of Central Shaft = Diameter of Pipe + (Thickness x 2)",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Outer Diameter of Central Shaft = " +str(round(calOfCentralPipeAndShaft.diameterOfCentralShaft, 1)) + " m",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Area of Central Shaft = " + str(round(calOfCentralPipeAndShaft.areaofCentralShaft, 2)) + " m^2",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "             ",
                    ln = 4, align = 'L')
                pdf.cell(200, 10, txt = "Step 3 : Calculation of Cascade Aerator Area - ",
                    ln = 3, align = 'L')
                pdf.cell(200,10, txt = "          Total Area of Cascade Aerator = Area of Cascade + Area of Shaft",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Total Area of Cascade Aerator = " + str(round(calOfCascade.totalAreaOfCascade,2)) + " m^2",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Diameter of Cascade Aerator = " +str(round(calOfCascade.diameterOfTotalCascade,2)) + " m",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "             ",
                    ln = 4, align = 'L')
                pdf.cell(200, 10, txt = "Step 4 : Diameter of Steps - ",
                    ln = 3, align = 'L')
                pdf.cell(200,10, txt = "          Assume The Height of Aerator = " + str(data.heightOfAerator) + " m",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Number of Risers = " + str(data.numberOfRisers),
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Height of Each Risers = " + str(round((data.heightOfEachRiser), 2)) + " m",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Diameter of Tip = Diameter of Bottom Cascade + No. of Risers",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Diameter of Tip = " +str(round((dimensionOfAerator.diameterOfTip),2)) + " m",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Check, Diameter of Tip > Diameter of Central Pipe",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Because, " +str(round((dimensionOfAerator.diameterOfTip),2)) + " m > " +str(round(calOfCentralPipeAndShaft.diameterOfCentralPipe, 1)) + " m",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Therefore, Check Satisfied",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Diameter 1st to " + str(data.numberOfSteps) + "th Cascade (in meter)  " ,
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "                = " +str(calOfCascade.d),
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "             ",
                    ln = 4, align = 'L')   
                pdf.cell(200, 10, txt = "Step 5 : Calculation of Launder - ",
                    ln = 3, align = 'L')
                pdf.cell(200,10, txt = "          Assume The Velocity Through Channel = " +str(data.velocityThroughChannel) + " m/s",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Now, discharge through the cascade will flow from both sides.",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          The Flow Rate Value = Q / 2" ,
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          The Flow Rate Value = " +str(round(calOfLaunder.flowRateValue, 2)) + " m^3/s" ,
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Flow Rate = A x V "  ,
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          A = " +str(round((calOfLaunder.flowRateValue/data.velocityThroughChannel),2)) + " m^2",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Here, "  ,
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          We assume, Width / Depth = " + str(data.widthToDepth) ,
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          So, Width = Depth ",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Therefore, " + "Width = " +str(round(calOfLaunder.width, 2)) + " m" + " & " "Depth = " +str(round(calOfLaunder.depth, 2)) + " m",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Now, assume free board provided to launder = " +str(data.freeBoardToLaunder) + " m",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Total Depth of Collection Launder = Depth + Free Board = " +str(round(calOfLaunder.depth, 2)) + " m",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "          Side Water Depth of Collection Launder = " +str(round(calOfLaunder.depth, 2)) + " m",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "             ",
                    ln = 4, align = 'L')
                pdf.cell(200, 10, txt = "*DESIGN SUMMARY : - ",
                    ln = 3, align = 'L')
                pdf.cell(200,10, txt = "       1. Area of Cascade : - " +str(round(areaOfCascade.areaOfCascadeAerator, 2)) + " m^2",
                    ln = 4, align = 'L')
                pdf.cell(200,10, txt = "       2. Diameter of Central Pipe : - " +str(round(calOfCentralPipeAndShaft.diameterOfCentralPipe, 1)) + " m",
                    ln = 5, align = 'L')
                pdf.cell(200,10, txt = "       3. Diameter of Central Shaft : - "+str(round(calOfCentralPipeAndShaft.diameterOfCentralShaft, 1)) + " m",
                    ln = 6, align = 'L')
                pdf.cell(200,10, txt = "       4. Diameter of Total Cascade Aerator : - "+str(round(calOfCascade.diameterOfTotalCascade,0)) + " m",
                    ln = 7, align = 'L')
                pdf.cell(200,10, txt = "       5. Flow Rate Vlaue : - "+str(round(calOfLaunder.flowRateValue, 2)) + " m^3/s",
                    ln = 8, align = 'L')
                pdf.cell(200,10, txt = "       6. Width of Launder : - "+str(round(calOfLaunder.width, 2)) + " m",
                    ln = 9, align = 'L')
                pdf.cell(200,10, txt = "       7. Depth of Launder : - "+str(round(calOfLaunder.depth, 2)) + " m",
                    ln = 10, align = 'L')
                pdf.cell(200,10, txt = "       8. Velocity of Water Through The Cascade : - "+str(round(data.velocityOfWaterThroughTheCascade)) + " m",
                    ln = 11, align = 'L')
                pdf.cell(200,10, txt = "       9. Rise of Cascade : - "+str(round(data.heightOfEachRiser, 2)) + " m",
                    ln = 12, align = 'L')
                pdf.cell(200,10, txt = "       10. Trade of Cascade : - "+str(round(calOfCascade.lengthOfEachTrade, 2)) + " m",
                    ln = 13, align = 'L')
                pdf.cell(200,10, txt = "       11. Number of Steps Provided in Cascade : - "+str(round(data.numberOfRisers)) + " Nos",
                    ln = 14, align = 'L')
                pdf.cell(200,10, txt = "       12. Height of Aerator : - "+str(round(data.heightOfAerator)) + " m",
                    ln = 14, align = 'L')
                pdf.output("EE_1_PBL_Group_1_"+str(round(discharge.inputDischargeInMLD, 0))+ " MLD" +".pdf")
            finalPrintToPDF()
            print("-----------------------------------------------------------------------------------------------------------------------")
            raw_input=str(input('PRESS ENTER TO GET PDF!'))
            print("-----------------------------------------------------------------------------------------------------------------------")
            def endpro():
                os.system('cls')
                Repeat = input("Do You Want to Design another Aerator ? (yes/no)")
                if Repeat == "yes":
                    os.system('cls')
                    main()
                else:
                    print("Thank You....")
                    raw_input=str(input('PRESS ENTER TO EXIT'))
                    exit()
            endpro()
        if choiceMainMenu.choice==2:
            os.system('cls')
            print("-----------------------------------------------------------------------------------------------------------------------")
            print(" - Assumptions Section")
            print("-----------------------------------------------------------------------------------------------------------------------")

            def data():
                data.surfaceLoadingRate=0.04 #m^2/m^3/hr IT HAS RANGE (0.02 - 0.05)
                data.velocityOfCentralPipe=1 #1 m/s
                data.velocityThroughChannel=1 #1 m/s
                data.velocityOfWaterThroughTheCascade=1 #1 m/s
                data.pi=3.14 #for calculation area of circle
                data.thicknessOfCentralShaft=0.3 #0.3m
                data.numberOfSteps=10 #10 steps
                data.widthToDepth=1 #Width to depth ratio
                data.width=1 #from width to depth ratio
                data.depth=1 #from widht to depth ratio
                data.freeBoardToLaunder=0.4 #Free board provided to launder is 0.4
                data.heightOfAerator=5 #Assume the height of aerator is 5m
                data.numberOfRisers=11 #No. Riser to be provided is 11
                data.heightOfEachRiser=(data.heightOfAerator/data.numberOfRisers)
                print("Surface Loading Rate = " + str(data.surfaceLoadingRate)+ " m^2/m^3/hr")
                print("Velocity of Central Pipe = " + str(data.velocityOfCentralPipe) +" m/s")
                print("Velocity Through Channel = " + str(data.velocityThroughChannel) + " m/s")
                print("Velocity Of Water Through Cascade = " + str(data.velocityOfWaterThroughTheCascade) + " m/s")
                print("Thickness Of Central Shaft = " + str(data.thicknessOfCentralShaft) + " m")
                print("Number Of Steps = " + str(data.numberOfSteps)+ " Nos")
                print("Free Board To Launder = " + str(data.freeBoardToLaunder) + " m")
                print("Height Of Aerator = " + str(data.heightOfAerator) + " m")
                print("Number of Risers = " + str(data.numberOfRisers)+ " Nos")
            data()

            def showAssumptions():
                print("-----------------------------------------------------------------------------------------------------------------------")
                change=str(input("Do You Want to change Assumption ? (yes/no)"))
                print("-----------------------------------------------------------------------------------------------------------------------")
                if change=="yes":
                    os.system('cls')
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print(" - Changing")
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    def data():
                        data.surfaceLoadingRate=float(input("Surface Loading Rate = "))
                        data.velocityOfCentralPipe=float(input("Velocity of Central Pipe = "))
                        data.velocityThroughChannel=float(input("Velocity Through Channel = "))
                        data.velocityOfWaterThroughTheCascade=float(input("Velocity Of Water Through Cascade = "))
                        data.pi=3.14 #for calculation area of circle
                        data.thicknessOfCentralShaft=float(input("Thickness Of Central Shaft = "))
                        data.numberOfSteps=int(input("Number Of Steps = "))
                        data.widthToDepth=1 #Width to depth ratio
                        data.width=1 #from width to depth ratio
                        data.depth=1 #from widht to depth ratio
                        data.freeBoardToLaunder=float(input("Free Board To Launder = "))
                        data.heightOfAerator=float(input("Height Of Aerator = "))
                        data.numberOfRisers=int(input("Number of Risers = "))
                        data.heightOfEachRiser=(data.heightOfAerator/data.numberOfRisers)
                    data()

                    def discharge():
                        discharge.inputDischargeInMLD=int(input("Enter the Rate of Flow (MLD) : - "))
                        discharge.flowRate=((discharge.inputDischargeInMLD*10**3)/24)
                        discharge.discharge=discharge.flowRate/(60*60)
                        print("Flow Rate = " + str(round(discharge.flowRate, 3)) + " m^3/hr")
                        print("Q = " + str(round(discharge.discharge, 3)) + " m^3/s")
                    discharge()

                    def areaOfCascade():
                        areaOfCascade.areaOfCascadeAerator=data.surfaceLoadingRate * discharge.flowRate
                        print("Area of Cascade Aerator = " + str(round(areaOfCascade.areaOfCascadeAerator, 3)) + " m^2")
                        #areaOfCascade.diameterOfCascadeAerator=(areaOfCascade.areaOfCascadeAerator/(data.pi/4))**(1/2)
                        #print("Diameter of Cascade = " +str(round(areaOfCascade.diameterOfCascadeAerator, 3)) + " m")
                    areaOfCascade()

                    def calOfCentralPipeAndShaft():
                        calOfCentralPipeAndShaft.areaOfCentralPipe=(discharge.discharge)/(data.velocityOfCentralPipe)
                        print("Area of Central Pipe = " + str(round(calOfCentralPipeAndShaft.areaOfCentralPipe, 3)) +" m^2")
                        calOfCentralPipeAndShaft.diameterOfCentralPipe=((calOfCentralPipeAndShaft.areaOfCentralPipe)/(data.pi/4))**(1/2)
                        print("Diameter of Central Pipe = " + str(round(calOfCentralPipeAndShaft.diameterOfCentralPipe, 1)) + " m")
                        calOfCentralPipeAndShaft.diameterOfCentralShaft=calOfCentralPipeAndShaft.diameterOfCentralPipe + (data.thicknessOfCentralShaft*2)
                        print("Diameter of Central Shaft = " + str(round(calOfCentralPipeAndShaft.diameterOfCentralShaft, 1)) + " m") 
                        calOfCentralPipeAndShaft.areaofCentralShaft=(((data.pi)/(4))*((calOfCentralPipeAndShaft.diameterOfCentralShaft)**(2)))
                        print("Area of Central Shaft = " + str(round(calOfCentralPipeAndShaft.areaofCentralShaft, 2)) + " m^2")
                    calOfCentralPipeAndShaft()

                    def calOfCascade():
                        calOfCascade.totalAreaOfCascade=(areaOfCascade.areaOfCascadeAerator + calOfCentralPipeAndShaft.areaofCentralShaft)
                        print("Total Area of Cascade = " + str(round(calOfCascade.totalAreaOfCascade,2)) + " m^2")
                        calOfCascade.diameterOfTotalCascade=((calOfCascade.totalAreaOfCascade)/(data.pi/4))**(1/2)
                        print("Diameter of Cascade Aerator = " + str(round(calOfCascade.diameterOfTotalCascade, 2)) + " m")
                        #Setps in Cascade Aerator
                        calOfCascade.d=[]
                        n=2
                        for i in range(0, data.numberOfSteps):
                            valD=(n)*3.51
                            n+=1
                            valD1=round(valD, 2)
                            calOfCascade.d.append(valD1)
                        print("Diameter of Cascade 1st to " + str(data.numberOfSteps) + " th")
                        print(calOfCascade.d)
                        print(calOfCascade.d[data.numberOfSteps-1])
                        print("Diameter of Cascade Aerator = " + str(round(calOfCascade.diameterOfTotalCascade, 2)) + " m " + "=" " Diameter of Bottom Cascade = " + str(round((calOfCascade.d[data.numberOfSteps-1]))) + " m")
                        checkDifference=(round((calOfCascade.d[data.numberOfSteps-1]))) - (round(calOfCascade.diameterOfTotalCascade, 2))
                        if checkDifference > 0.30:
                            print("#Condition/Check not Satisfied")
                        elif checkDifference < 0.30:
                            print("#Contidion/Check Satisfied")
                        else:
                            print("Error !")
                        calOfCascade.lengthOfEachTrade=((calOfCascade.d[data.numberOfSteps-1])/2)/11
                    calOfCascade()

                    def dimensionOfAerator():
                        dimensionOfAerator.diameterOfTip=(calOfCascade.diameterOfTotalCascade/data.numberOfRisers)
                        print("Diameter of Tip = " + str(round(dimensionOfAerator.diameterOfTip,2)) + " m")
                        print("Check, Diameter of tip > Diameter of Central Pipe")
                        if dimensionOfAerator.diameterOfTip > calOfCentralPipeAndShaft.diameterOfCentralPipe:
                            print("Condition/Check Satisfied")
                        else:
                            print("Error !")
                    dimensionOfAerator()

                    def calOfLaunder():
                        calOfLaunder.flowRateValue=((round(discharge.discharge, 3))/2)
                        print("The Flow Rate Value = " + str(round(calOfLaunder.flowRateValue, 3)) + " m^3/s")
                        calOfLaunder.area=(calOfLaunder.flowRateValue)/(data.velocityThroughChannel)
                        print("Area of Launder = " +str(round(calOfLaunder.area, 3)) + " m")
                        calOfLaunder.width=calOfLaunder.area/(data.depth+data.depth)
                        calOfLaunder.depthWithoutLaunder=calOfLaunder.area/(data.width+data.width)
                        calOfLaunder.depth=round((calOfLaunder.depthWithoutLaunder+data.freeBoardToLaunder),3)
                        print("Width of Launder = " + str(round(calOfLaunder.width, 3)) + " m")
                        print("Depth of Launder = " + str(round(calOfLaunder.depth, 3)) + " m")
                    calOfLaunder()

                    def finalOutput():
                        print("-----------------------------------------------------------------------------------------------------------------------")
                        print(" - Design Summary")
                        print("-----------------------------------------------------------------------------------------------------------------------")
                        print("1. Area of Cascade : " + str(round(areaOfCascade.areaOfCascadeAerator, 3)) + " m^2")
                        print("2. Diameter of Central Pipe : " + str(round(calOfCentralPipeAndShaft.diameterOfCentralPipe, 1)) + " m")
                        print("3. Diameter of Central Shaft : " + str(round(calOfCentralPipeAndShaft.diameterOfCentralShaft, 1)) + " m") 
                        print("4. Diameter of total cascade aerator : " + str(round(calOfCascade.diameterOfTotalCascade, 0)) + " m")
                        print("5. Flow Rate Value : " + str(round(calOfLaunder.flowRateValue, 3)) + " m^3/s")
                        print("6. Width of Launder : " + str(round(calOfLaunder.width, 3)) + " m")
                        print("7. Depth of Launder : " + str(round(calOfLaunder.depth, 3)) + " m")
                        print("8. Velocity of Water Through the cascade : " + str(data.velocityOfWaterThroughTheCascade) + " m")
                        print("9. Rise of Cascade : " + str(round(data.heightOfEachRiser, 2)) + " m")
                        print("10. Trade of Cascade : "+ str(round(calOfCascade.lengthOfEachTrade, 2))+ " m")
                        print("11. Number of Steps provided in cascade : " + str(round(data.numberOfRisers)) + " Nos")
                        print("12. Height of Aerator is : "+str(data.heightOfAerator) + " m" )
                    finalOutput()
                    def finalPrintToPDF():
                        pdf = FPDF() #Making a PDF Variable
                        pdf.add_page() #Adding a Page
                        pdf.set_font("Arial" , size= 15) #Font ani Size
                        #Actual Printing in PDF Starts here...........
                        pdf.cell(200, 10, txt = "Design Of Cascade Aerator",
                            ln = 1, align = 'C')
                        pdf.cell(200, 10, txt = "(" +str(round(discharge.inputDischargeInMLD, 0))+ " MLD" ")",
                            ln = 2, align = 'C')
                        pdf.cell(200, 10, txt = "GIVEN : - ",
                            ln = 3, align = 'L')    
                        pdf.cell(200,10, txt = "          Q = " +str(discharge.inputDischargeInMLD) + " MLD",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "              = " +str((discharge.inputDischargeInMLD)*10**6) + " l/d",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "              = " +str((discharge.inputDischargeInMLD)*(10**6)*(10**-3)) + " m^3/d",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "              = " +str(round((((discharge.inputDischargeInMLD)*10**3)/24), 3)) + " m^3/hr",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "              = " +str((((discharge.inputDischargeInMLD)*10**3)/24)/(60*60)) + " m^3/s",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "             ",
                            ln = 4, align = 'L')
                        pdf.cell(200, 10, txt = "Step 1 : Determination of Aera of Cascade Aerator - ",
                            ln = 3, align = 'L')
                        pdf.cell(200,10, txt = "          Surface Loading Rate = " +str(data.surfaceLoadingRate) + " m^2/m^3/hrs",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Flow Rate = " +str(round((((discharge.inputDischargeInMLD)*10**3)/24), 3)) + " m^3/hr",
                            ln = 4, align = 'L')   
                        pdf.cell(200,10, txt = "          Area of Cascade Aerator = Surface Loading Rate x Flow Rate",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Area of Cascade Aerator = " +str(round(areaOfCascade.areaOfCascadeAerator, 2)) + " m^2",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "             ",
                            ln = 4, align = 'L')
                        pdf.cell(200, 10, txt = "Step 2 : Calculation For The Diameter of Central Pipe and Shaft - ",
                            ln = 3, align = 'L')
                        pdf.cell(200,10, txt = "          Assume the Velocity of Central Pipe = " +str(data.velocityOfCentralPipe) + " m/s",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          By continuity equation, ",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Q = A x V ",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          A = Q x V ",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          A = " +str(round((discharge.inputDischargeInMLD/data.velocityOfCentralPipe),3)) + " m^2",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          A = (pi/4) x Diameter of Central Pipe ",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Diameter of Central Pipe = " +str(round(calOfCentralPipeAndShaft.diameterOfCentralPipe, 1)) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Now, Assume the thickness of Central Shaft = " +str(data.thicknessOfCentralShaft) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Outer Diameter of Central Shaft = Diameter of Pipe + (Thickness x 2)",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Outer Diameter of Central Shaft = " +str(round(calOfCentralPipeAndShaft.diameterOfCentralShaft, 1)) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Area of Central Shaft = " + str(round(calOfCentralPipeAndShaft.areaofCentralShaft, 2)) + " m^2",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "             ",
                            ln = 4, align = 'L')
                        pdf.cell(200, 10, txt = "Step 3 : Calculation of Cascade Aerator Area - ",
                            ln = 3, align = 'L')
                        pdf.cell(200,10, txt = "          Total Area of Cascade Aerator = Area of Cascade + Area of Shaft",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Total Area of Cascade Aerator = " + str(round(calOfCascade.totalAreaOfCascade,2)) + " m^2",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Diameter of Cascade Aerator = " +str(round(calOfCascade.diameterOfTotalCascade,2)) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "             ",
                            ln = 4, align = 'L')
                        pdf.cell(200, 10, txt = "Step 4 : Diameter of Steps - ",
                            ln = 3, align = 'L')
                        pdf.cell(200,10, txt = "          Assume The Height of Aerator = " + str(data.heightOfAerator) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Number of Risers = " + str(data.numberOfRisers),
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Height of Each Risers = " + str(round((data.heightOfEachRiser), 2)) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Diameter of Tip = Diameter of Bottom Cascade + No. of Risers",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Diameter of Tip = " +str(round((dimensionOfAerator.diameterOfTip),2)) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Check, Diameter of Tip > Diameter of Central Pipe",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Because, " +str(round((dimensionOfAerator.diameterOfTip),2)) + " m > " +str(round(calOfCentralPipeAndShaft.diameterOfCentralPipe, 1)) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Therefore, Check Satisfied",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Diameter 1st to " + str(data.numberOfSteps) + "th Cascade (in meter)  " ,
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "                = " +str(calOfCascade.d),
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "             ",
                            ln = 4, align = 'L')   
                        pdf.cell(200, 10, txt = "Step 5 : Calculation of Launder - ",
                            ln = 3, align = 'L')
                        pdf.cell(200,10, txt = "          Assume The Velocity Through Channel = " +str(data.velocityThroughChannel) + " m/s",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Now, discharge through the cascade will flow from both sides.",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          The Flow Rate Value = Q / 2" ,
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          The Flow Rate Value = " +str(round(calOfLaunder.flowRateValue, 2)) + " m^3/s" ,
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Flow Rate = A x V "  ,
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          A = " +str(round((calOfLaunder.flowRateValue/data.velocityThroughChannel),2)) + " m^2",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Here, "  ,
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          We assume, Width / Depth = " + str(data.widthToDepth) ,
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          So, Width = Depth ",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Therefore, " + "Width = " +str(round(calOfLaunder.width, 2)) + " m" + " & " "Depth = " +str(round(calOfLaunder.depth, 2)) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Now, assume free board provided to launder = " +str(data.freeBoardToLaunder) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Total Depth of Collection Launder = Depth + Free Board = " +str(round(calOfLaunder.depth, 2)) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Side Water Depth of Collection Launder = " +str(round(calOfLaunder.depth, 2)) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "             ",
                            ln = 4, align = 'L')
                        pdf.cell(200, 10, txt = "*DESIGN SUMMARY : - ",
                            ln = 3, align = 'L')
                        pdf.cell(200,10, txt = "       1. Area of Cascade : - " +str(round(areaOfCascade.areaOfCascadeAerator, 2)) + " m^2",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "       2. Diameter of Central Pipe : - " +str(round(calOfCentralPipeAndShaft.diameterOfCentralPipe, 1)) + " m",
                            ln = 5, align = 'L')
                        pdf.cell(200,10, txt = "       3. Diameter of Central Shaft : - "+str(round(calOfCentralPipeAndShaft.diameterOfCentralShaft, 1)) + " m",
                            ln = 6, align = 'L')
                        pdf.cell(200,10, txt = "       4. Diameter of Total Cascade Aerator : - "+str(round(calOfCascade.diameterOfTotalCascade,0)) + " m",
                            ln = 7, align = 'L')
                        pdf.cell(200,10, txt = "       5. Flow Rate Vlaue : - "+str(round(calOfLaunder.flowRateValue, 2)) + " m^3/s",
                            ln = 8, align = 'L')
                        pdf.cell(200,10, txt = "       6. Width of Launder : - "+str(round(calOfLaunder.width, 2)) + " m",
                            ln = 9, align = 'L')
                        pdf.cell(200,10, txt = "       7. Depth of Launder : - "+str(round(calOfLaunder.depth, 2)) + " m",
                            ln = 10, align = 'L')
                        pdf.cell(200,10, txt = "       8. Velocity of Water Through The Cascade : - "+str(round(data.velocityOfWaterThroughTheCascade)) + " m",
                            ln = 11, align = 'L')
                        pdf.cell(200,10, txt = "       9. Rise of Cascade : - "+str(round(data.heightOfEachRiser, 2)) + " m",
                            ln = 12, align = 'L')
                        pdf.cell(200,10, txt = "       10. Trade of Cascade : - "+str(round(calOfCascade.lengthOfEachTrade, 2)) + " m",
                            ln = 13, align = 'L')
                        pdf.cell(200,10, txt = "       11. Number of Steps Provided in Cascade : - "+str(round(data.numberOfRisers)) + " Nos",
                            ln = 14, align = 'L')
                        pdf.cell(200,10, txt = "       12. Height of Aerator : - "+str(round(data.heightOfAerator)) + " m",
                            ln = 14, align = 'L')
                        pdf.output("EE_1_PBL_Group_1_"+str(round(discharge.inputDischargeInMLD, 0))+ " MLD" +".pdf")
                    finalPrintToPDF()
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    raw_input=str(input('PRESS ENTER TO GET PDF!'))
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    def endpro():
                        os.system('cls')
                        Repeat = input("Do You Want to Design another Aerator ? (yes/no)")
                        if Repeat == "yes":
                            os.system('cls')
                            main()
                        else:
                            print("Thank You....")
                            raw_input=str(input('PRESS ENTER TO EXIT'))
                            exit()
                    endpro()
                elif change=="no":
                    os.system('cls')
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    print(" - No Change")
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    def data():
                        data.surfaceLoadingRate=0.04 #m^2/m^3/hr IT HAS RANGE (0.02 - 0.05)
                        data.velocityOfCentralPipe=1 #1 m/s
                        data.velocityThroughChannel=1 #1 m/s
                        data.velocityOfWaterThroughTheCascade=1 #1 m/s
                        data.pi=3.14 #for calculation area of circle
                        data.thicknessOfCentralShaft=0.3 #0.3m
                        data.numberOfSteps=10 #10 steps
                        data.widthToDepth=1 #Width to depth ratio
                        data.width=1 #from width to depth ratio
                        data.depth=1 #from widht to depth ratio
                        data.freeBoardToLaunder=0.4 #Free board provided to launder is 0.4
                        data.heightOfAerator=5 #Assume the height of aerator is 5m
                        data.numberOfRisers=11 #No. Riser to be provided is 11
                        data.heightOfEachRiser=(data.heightOfAerator/data.numberOfRisers)
                    data()
                    def discharge():
                        discharge.inputDischargeInMLD=int(input("Enter the Rate of Flow (MLD) : - "))
                        discharge.flowRate=((discharge.inputDischargeInMLD*10**3)/24)
                        discharge.discharge=discharge.flowRate/(60*60)
                        print("Flow Rate = " + str(round(discharge.flowRate, 3)) + " m^3/hr")
                        print("Q = " + str(round(discharge.discharge, 3)) + " m^3/s")
                    discharge()

                    def areaOfCascade():
                        areaOfCascade.areaOfCascadeAerator=data.surfaceLoadingRate * discharge.flowRate
                        print("Area of Cascade Aerator = " + str(round(areaOfCascade.areaOfCascadeAerator, 3)) + " m^2")
                        #areaOfCascade.diameterOfCascadeAerator=(areaOfCascade.areaOfCascadeAerator/(data.pi/4))**(1/2)
                        #print("Diameter of Cascade = " +str(round(areaOfCascade.diameterOfCascadeAerator, 3)) + " m")
                    areaOfCascade()

                    def calOfCentralPipeAndShaft():
                        calOfCentralPipeAndShaft.areaOfCentralPipe=(discharge.discharge)/(data.velocityOfCentralPipe)
                        print("Area of Central Pipe = " + str(round(calOfCentralPipeAndShaft.areaOfCentralPipe, 3)) +" m^2")
                        calOfCentralPipeAndShaft.diameterOfCentralPipe=((calOfCentralPipeAndShaft.areaOfCentralPipe)/(data.pi/4))**(1/2)
                        print("Diameter of Central Pipe = " + str(round(calOfCentralPipeAndShaft.diameterOfCentralPipe, 1)) + " m")
                        calOfCentralPipeAndShaft.diameterOfCentralShaft=calOfCentralPipeAndShaft.diameterOfCentralPipe + (data.thicknessOfCentralShaft*2)
                        print("Diameter of Central Shaft = " + str(round(calOfCentralPipeAndShaft.diameterOfCentralShaft, 1)) + " m") 
                        calOfCentralPipeAndShaft.areaofCentralShaft=(((data.pi)/(4))*((calOfCentralPipeAndShaft.diameterOfCentralShaft)**(2)))
                        print("Area of Central Shaft = " + str(round(calOfCentralPipeAndShaft.areaofCentralShaft, 2)) + " m^2")
                    calOfCentralPipeAndShaft()

                    def calOfCascade():
                        calOfCascade.totalAreaOfCascade=(areaOfCascade.areaOfCascadeAerator + calOfCentralPipeAndShaft.areaofCentralShaft)
                        print("Total Area of Cascade = " + str(round(calOfCascade.totalAreaOfCascade,2)) + " m^2")
                        calOfCascade.diameterOfTotalCascade=((calOfCascade.totalAreaOfCascade)/(data.pi/4))**(1/2)
                        print("Diameter of Cascade Aerator = " + str(round(calOfCascade.diameterOfTotalCascade, 2)) + " m")
                        #Setps in Cascade Aerator
                        calOfCascade.d=[]
                        n=2
                        for i in range(0, data.numberOfSteps):
                            valD=(n)*3.51
                            n+=1
                            valD1=round(valD, 2)
                            calOfCascade.d.append(valD1)
                        print("Diameter of Cascade 1st to " + str(data.numberOfSteps) + " th")
                        print(calOfCascade.d)
                        print(calOfCascade.d[data.numberOfSteps-1])
                        print("Diameter of Cascade Aerator = " + str(round(calOfCascade.diameterOfTotalCascade, 2)) + " m " + "=" " Diameter of Bottom Cascade = " + str(round((calOfCascade.d[data.numberOfSteps-1]))) + " m")
                        checkDifference=(round((calOfCascade.d[data.numberOfSteps-1]))) - (round(calOfCascade.diameterOfTotalCascade, 2))
                        if checkDifference > 0.30:
                            print("#Condition/Check not Satisfied")
                        elif checkDifference < 0.30:
                            print("#Contidion/Check Satisfied")
                        else:
                            print("Error !")
                        calOfCascade.lengthOfEachTrade=((calOfCascade.d[data.numberOfSteps-1])/2)/11
                    calOfCascade()

                    def dimensionOfAerator():
                        dimensionOfAerator.diameterOfTip=(calOfCascade.diameterOfTotalCascade/data.numberOfRisers)
                        print("Diameter of Tip = " + str(round(dimensionOfAerator.diameterOfTip,2)) + " m")
                        print("Check, Diameter of tip > Diameter of Central Pipe")
                        if dimensionOfAerator.diameterOfTip > calOfCentralPipeAndShaft.diameterOfCentralPipe:
                            print("Condition/Check Satisfied")
                        else:
                            print("Error !")
                    dimensionOfAerator()

                    def calOfLaunder():
                        calOfLaunder.flowRateValue=((round(discharge.discharge, 3))/2)
                        print("The Flow Rate Value = " + str(round(calOfLaunder.flowRateValue, 3)) + " m^3/s")
                        calOfLaunder.area=(calOfLaunder.flowRateValue)/(data.velocityThroughChannel)
                        print("Area of Launder = " +str(round(calOfLaunder.area, 3)) + " m")
                        calOfLaunder.width=calOfLaunder.area/(data.depth+data.depth)
                        calOfLaunder.depthWithoutLaunder=calOfLaunder.area/(data.width+data.width)
                        calOfLaunder.depth=round((calOfLaunder.depthWithoutLaunder+data.freeBoardToLaunder),3)
                        print("Width of Launder = " + str(round(calOfLaunder.width, 3)) + " m")
                        print("Depth of Launder = " + str(round(calOfLaunder.depth, 3)) + " m")
                    calOfLaunder()

                    def finalOutput():
                        print("-----------------------------------------------------------------------------------------------------------------------")
                        print(" - Design Summary")
                        print("-----------------------------------------------------------------------------------------------------------------------")
                        print("1. Area of Cascade : " + str(round(areaOfCascade.areaOfCascadeAerator, 3)) + " m^2")
                        print("2. Diameter of Central Pipe : " + str(round(calOfCentralPipeAndShaft.diameterOfCentralPipe, 1)) + " m")
                        print("3. Diameter of Central Shaft : " + str(round(calOfCentralPipeAndShaft.diameterOfCentralShaft, 1)) + " m") 
                        print("4. Diameter of total cascade aerator : " + str(round(calOfCascade.diameterOfTotalCascade, 0)) + " m")
                        print("5. Flow Rate Value : " + str(round(calOfLaunder.flowRateValue, 3)) + " m^3/s")
                        print("6. Width of Launder : " + str(round(calOfLaunder.width, 3)) + " m")
                        print("7. Depth of Launder : " + str(round(calOfLaunder.depth, 3)) + " m")
                        print("8. Velocity of Water Through the cascade : " + str(data.velocityOfWaterThroughTheCascade) + " m")
                        print("9. Rise of Cascade : " + str(round(data.heightOfEachRiser, 2)) + " m")
                        print("10. Trade of Cascade : "+ str(round(calOfCascade.lengthOfEachTrade, 2))+ " m")
                        print("11. Number of Steps provided in cascade : " + str(round(data.numberOfRisers)) + " Nos")
                        print("12. Height of Aerator is : "+str(data.heightOfAerator) + " m" )
                    finalOutput()
                    def finalPrintToPDF():
                        pdf = FPDF() #Making a PDF Variable
                        pdf.add_page() #Adding a Page
                        pdf.set_font("Arial" , size= 15) #Font ani Size
                        #Actual Printing in PDF Starts here...........
                        pdf.cell(200, 10, txt = "Design Of Cascade Aerator",
                            ln = 1, align = 'C')
                        pdf.cell(200, 10, txt = "(" +str(round(discharge.inputDischargeInMLD, 0))+ " MLD" ")",
                            ln = 2, align = 'C')
                        pdf.cell(200, 10, txt = "GIVEN : - ",
                            ln = 3, align = 'L')    
                        pdf.cell(200,10, txt = "          Q = " +str(discharge.inputDischargeInMLD) + " MLD",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "              = " +str((discharge.inputDischargeInMLD)*10**6) + " l/d",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "              = " +str((discharge.inputDischargeInMLD)*(10**6)*(10**-3)) + " m^3/d",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "              = " +str(round((((discharge.inputDischargeInMLD)*10**3)/24), 3)) + " m^3/hr",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "              = " +str((((discharge.inputDischargeInMLD)*10**3)/24)/(60*60)) + " m^3/s",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "             ",
                            ln = 4, align = 'L')
                        pdf.cell(200, 10, txt = "Step 1 : Determination of Aera of Cascade Aerator - ",
                            ln = 3, align = 'L')
                        pdf.cell(200,10, txt = "          Surface Loading Rate = " +str(data.surfaceLoadingRate) + " m^2/m^3/hrs",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Flow Rate = " +str(round((((discharge.inputDischargeInMLD)*10**3)/24), 3)) + " m^3/hr",
                            ln = 4, align = 'L')   
                        pdf.cell(200,10, txt = "          Area of Cascade Aerator = Surface Loading Rate x Flow Rate",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Area of Cascade Aerator = " +str(round(areaOfCascade.areaOfCascadeAerator, 2)) + " m^2",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "             ",
                            ln = 4, align = 'L')
                        pdf.cell(200, 10, txt = "Step 2 : Calculation For The Diameter of Central Pipe and Shaft - ",
                            ln = 3, align = 'L')
                        pdf.cell(200,10, txt = "          Assume the Velocity of Central Pipe = " +str(data.velocityOfCentralPipe) + " m/s",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          By continuity equation, ",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Q = A x V ",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          A = Q x V ",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          A = " +str(round((discharge.inputDischargeInMLD/data.velocityOfCentralPipe),3)) + " m^2",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          A = (pi/4) x Diameter of Central Pipe ",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Diameter of Central Pipe = " +str(round(calOfCentralPipeAndShaft.diameterOfCentralPipe, 1)) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Now, Assume the thickness of Central Shaft = " +str(data.thicknessOfCentralShaft) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Outer Diameter of Central Shaft = Diameter of Pipe + (Thickness x 2)",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Outer Diameter of Central Shaft = " +str(round(calOfCentralPipeAndShaft.diameterOfCentralShaft, 1)) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Area of Central Shaft = " + str(round(calOfCentralPipeAndShaft.areaofCentralShaft, 2)) + " m^2",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "             ",
                            ln = 4, align = 'L')
                        pdf.cell(200, 10, txt = "Step 3 : Calculation of Cascade Aerator Area - ",
                            ln = 3, align = 'L')
                        pdf.cell(200,10, txt = "          Total Area of Cascade Aerator = Area of Cascade + Area of Shaft",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Total Area of Cascade Aerator = " + str(round(calOfCascade.totalAreaOfCascade,2)) + " m^2",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Diameter of Cascade Aerator = " +str(round(calOfCascade.diameterOfTotalCascade,2)) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "             ",
                            ln = 4, align = 'L')
                        pdf.cell(200, 10, txt = "Step 4 : Diameter of Steps - ",
                            ln = 3, align = 'L')
                        pdf.cell(200,10, txt = "          Assume The Height of Aerator = " + str(data.heightOfAerator) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Number of Risers = " + str(data.numberOfRisers),
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Height of Each Risers = " + str(round((data.heightOfEachRiser), 2)) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Diameter of Tip = Diameter of Bottom Cascade + No. of Risers",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Diameter of Tip = " +str(round((dimensionOfAerator.diameterOfTip),2)) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Check, Diameter of Tip > Diameter of Central Pipe",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Because, " +str(round((dimensionOfAerator.diameterOfTip),2)) + " m > " +str(round(calOfCentralPipeAndShaft.diameterOfCentralPipe, 1)) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Therefore, Check Satisfied",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Diameter 1st to " + str(data.numberOfSteps) + "th Cascade (in meter)  " ,
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "                = " +str(calOfCascade.d),
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "             ",
                            ln = 4, align = 'L')   
                        pdf.cell(200, 10, txt = "Step 5 : Calculation of Launder - ",
                            ln = 3, align = 'L')
                        pdf.cell(200,10, txt = "          Assume The Velocity Through Channel = " +str(data.velocityThroughChannel) + " m/s",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Now, discharge through the cascade will flow from both sides.",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          The Flow Rate Value = Q / 2" ,
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          The Flow Rate Value = " +str(round(calOfLaunder.flowRateValue, 2)) + " m^3/s" ,
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Flow Rate = A x V "  ,
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          A = " +str(round((calOfLaunder.flowRateValue/data.velocityThroughChannel),2)) + " m^2",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Here, "  ,
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          We assume, Width / Depth = " + str(data.widthToDepth) ,
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          So, Width = Depth ",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Therefore, " + "Width = " +str(round(calOfLaunder.width, 2)) + " m" + " & " "Depth = " +str(round(calOfLaunder.depth, 2)) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Now, assume free board provided to launder = " +str(data.freeBoardToLaunder) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Total Depth of Collection Launder = Depth + Free Board = " +str(round(calOfLaunder.depth, 2)) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "          Side Water Depth of Collection Launder = " +str(round(calOfLaunder.depth, 2)) + " m",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "             ",
                            ln = 4, align = 'L')
                        pdf.cell(200, 10, txt = "*DESIGN SUMMARY : - ",
                            ln = 3, align = 'L')
                        pdf.cell(200,10, txt = "       1. Area of Cascade : - " +str(round(areaOfCascade.areaOfCascadeAerator, 2)) + " m^2",
                            ln = 4, align = 'L')
                        pdf.cell(200,10, txt = "       2. Diameter of Central Pipe : - " +str(round(calOfCentralPipeAndShaft.diameterOfCentralPipe, 1)) + " m",
                            ln = 5, align = 'L')
                        pdf.cell(200,10, txt = "       3. Diameter of Central Shaft : - "+str(round(calOfCentralPipeAndShaft.diameterOfCentralShaft, 1)) + " m",
                            ln = 6, align = 'L')
                        pdf.cell(200,10, txt = "       4. Diameter of Total Cascade Aerator : - "+str(round(calOfCascade.diameterOfTotalCascade,0)) + " m",
                            ln = 7, align = 'L')
                        pdf.cell(200,10, txt = "       5. Flow Rate Vlaue : - "+str(round(calOfLaunder.flowRateValue, 2)) + " m^3/s",
                            ln = 8, align = 'L')
                        pdf.cell(200,10, txt = "       6. Width of Launder : - "+str(round(calOfLaunder.width, 2)) + " m",
                            ln = 9, align = 'L')
                        pdf.cell(200,10, txt = "       7. Depth of Launder : - "+str(round(calOfLaunder.depth, 2)) + " m",
                            ln = 10, align = 'L')
                        pdf.cell(200,10, txt = "       8. Velocity of Water Through The Cascade : - "+str(round(data.velocityOfWaterThroughTheCascade)) + " m",
                            ln = 11, align = 'L')
                        pdf.cell(200,10, txt = "       9. Rise of Cascade : - "+str(round(data.heightOfEachRiser, 2)) + " m",
                            ln = 12, align = 'L')
                        pdf.cell(200,10, txt = "       10. Trade of Cascade : - "+str(round(calOfCascade.lengthOfEachTrade, 2)) + " m",
                            ln = 13, align = 'L')
                        pdf.cell(200,10, txt = "       11. Number of Steps Provided in Cascade : - "+str(round(data.numberOfRisers)) + " Nos",
                            ln = 14, align = 'L')
                        pdf.cell(200,10, txt = "       12. Height of Aerator : - "+str(round(data.heightOfAerator)) + " m",
                            ln = 14, align = 'L')
                        pdf.output("EE_1_PBL_Group_1_"+str(round(discharge.inputDischargeInMLD, 0))+ " MLD" +".pdf")
                    finalPrintToPDF()
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    raw_input=str(input('PRESS ENTER TO GET PDF!'))
                    print("-----------------------------------------------------------------------------------------------------------------------")
                    def endpro():
                        os.system('cls')
                        Repeat = input("Do You Want to Design another Aerator ? (yes/no)")
                        if Repeat == "yes":
                            os.system('cls')
                            main()
                        else:
                            print("Thank You....")
                            raw_input=str(input('PRESS ENTER TO EXIT'))
                            exit()
                    endpro()
                else:
                    print("Error !")
            showAssumptions()
        if choiceMainMenu.choice==3:
            exit()
        else:
            print("Unexpected Input !")
            choiceMainMenu()
    choiceMainMenu()
main()
#Use below line 
#os.system('mode con: cols=100 lines=40') 


