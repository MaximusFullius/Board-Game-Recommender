print("BOARD GAME FINDER by Maxwell R. Fuller")
print("Answer the questions with either of the given option words given in this format: (a/b)")
print("Make sure to ONLY input EXACTLY the first or second option!")
print("You will get a recommended board game based on the answers you provide. I hope this helps you have fun! \n")
    
strPlayingWithChildren = input("Are you playing with children? (y/n) \n")
if strPlayingWithChildren == "y":
      strYoungerThan7= input("Are the children younger than 7? (y/n) \n")
      if strYoungerThan7 == "y":
          strGirlsOnly = input("Girly girls only? (y/n) \n")
          if strGirlsOnly == "y":
              print("Your recommended board game is: Candy Land")
          elif strGirlsOnly == "n":
              strRealRules = input("Real rules or just for fun? (fun/rules) \n")
              if strRealRules == "rules":
                  strFunForAdults = input("Do you want the game to be fun for adults as well? (y/n) \n")
                  if strFunForAdults == "y":
                      print("Your recommended board game is: Sorry")
                  elif strFunForAdults == "n":
                      print("Your recommended board game is: Life")
              elif strRealRules == "fun":
                  strRubeGoldberg = input("Do you like Rube Goldberg Machines? (y/n) \n")
                  if strRubeGoldberg == "y":
                      print("Your recommended board game is: Mouse Trap")
                  elif strRubeGoldberg == "n":
                      print("Your recommended board game is: Operation")
      elif strYoungerThan7 == "n":
          strCrushingDefeat = input("Do you want to let the children experience crushing defeat? (y/n) \n")
          if strCrushingDefeat == "y":
              print("Your recommended board game is: Monopoly")
          elif strCrushingDefeat == "n":
              strPortable = input("Do you want the game to be portable? (y/n) \n")
              if strPortable == "y":
                  print("Your recommended board game is: Yahtzee!")
              elif strPortable == "n":
                  strWinTeam = input("One winner or team effort? (one/team) \n")
                  if strWinTeam == "one":
                      print("Your recommended board game is: Small World")
                  elif strWinTeam == "team":
                      print("Your recommended board game is: Forbidden Island")

elif strPlayingWithChildren == "n":
      strTwoHours = input("Do you want to play for more than two hours? (y/n) \n")
      if strTwoHours == "y":
          strHardRules = input("Do want a game with hard rules? (y/n) \n")
          if strHardRules == "y":
              print("Your recommended board game is: Axis and Allies")
          elif strHardRules == "n":
              strUntilEnd = input("Do you want a game where all players play until the end? (y/n) \n")
              if strUntilEnd == "y":
                  print("Your recommended board game is: Le Havre")
              elif strUntilEnd == "n":
                  strDiceOrStrat = input("Dice battles or 100% strategy? (dice/strat) \n")
                  if strDiceOrStrat == "dice":
                      print("Your recommended board game is: Risk")
                  elif strDiceOrStrat == "strat":
                      print("Your recommended board game is: Game of Thrones")
      elif strTwoHours == "n":
          strNerd = input("Are you a huge nerd? (y/n) \n")
          if strNerd == "y":
              strPrep = input("Do you want to spend dozens of hours preparing to play? (y/n) \n")
              if strPrep == "y":
                  print("Your recommended board game is: Warhammer")
              elif strPrep == "n":
                  strSpend = input("Are you willing to invest extra money into your game? (y/n) \n")
                  if strSpend == "y":
                      print("Your recommended board game is: Magic")
                  elif strSpend == "n":
                      strBoomer = input("Does the name 'Boomer' give you wet dreams? (y/n) \n")
                      if strBoomer == "y":
                          print("Your recommended board game is: Battlestar Galactica")
                      elif strBoomer == "n":
                                      print("Your recommended board game is: Cosmic Encounter")
          elif strNerd == "n":
              strGetAlong = input("Do you think everyone should just get along? (y/n) \n")
              if strGetAlong == "y":
                  strDick = input("Do you secretly wish you were a Dick (a P.I)? (y/n) \n")
                  if strDick == "y":
                      print("Your recommended board game is: Arkham Horror")
                  elif strDick == "n":
                      strMonty = input("Do you like Monty Python? (y/n) \n")
                      if strMonty == "y":
                          print("Your recommended board game is: Shadows over Camelot")
                      elif strMonty == "n":
                          strZombie = input("Do you like Zombies? (y/n) \n")
                          if strZombie == "y":
                              print("Your recommended board game is: Last Night on Earth")
                          elif strZombie == "n":
                              strMonsterVirus = input("Would you rather fight monsters or Viruses? (monster/virus) \n")
                              if strMonsterVirus == "monster":
                                  print("Your recommended board game is: Dungeon Run")
                              elif strMonsterVirus == "virus":
                                      print("Your recommended board game is: Pandemic")
              elif strGetAlong == "n":
                  strGamble = input("Do you like to gamble? (y/n) \n")
                  if strGamble == "y":
                          print("Your recommended board game is: Rummoli")
                  elif strGamble == "n":
                      strOver50 = input("Are you over 50 years old? (y/n) \n")
                      if strOver50 == "y":
                          strMoreThanTwo = input("Are there more than two players? (y/n) \n")
                          if strMoreThanTwo == "y":
                              print("Your recommended board game is: Cribbage")
                          elif strMoreThanTwo == "n":
                              strMensa = input("Are you smart? (y/n) \n")
                              if strMensa == "y":
                                  strCliche = input("Is Chess too cliche? (y/n) \n")
                                  if strCliche == "y":
                                      print("Your recommended board game is: Go")
                                  elif strCliche == "n":
                                      print("Your recommended board game is: Chess")
                              elif strMensa == "n":
                                  print("Your recommended board game is: Backgammon")
                      elif strOver50 == "n":
                          strParty = input("Are you looking for a Party Game? (y/n) \n")
                          if strParty == "y":
                              strLaid = input("Are you looking to get laid? (y/n) \n")
                              if strLaid == "y":
                                  print("Your recommended board game is: Twister")
                              elif strLaid == "n":
                                  strEmbarrass = input("Want to embarrass your friends? (y/n) \n")
                                  if strEmbarrass == "y":
                                      strThugArtist = input("Do you want to be a Thug or an Artist? (thug/artist) \n")
                                      if strThugArtist == "thug":
                                          print("Your recommended board game is: Ca$h'N'Gun$")
                                      elif strThugArtist == "artist":
                                          print("Your recommended board game is: Cranium")
                                  elif strEmbarrass == "n":
                                      strLiar = input("Are ypu a creative liar? (y/n) \n")
                                      if strLiar == "y":
                                          strWordsTrivia =  input("Words or Trivia? (words/trivia) \n")
                                          if strWordsTrivia == "words":
                                              print("Your recommended board game is: Beyond Balderdash")
                                          elif strWordsTrivia == "trivia":
                                              print("Your recommended board game is: Wits and Wagers")
                                      elif strLiar == "n":
                                          strHands = input("Are you good with your hands? (y/n) \n")
                                          if strHands == "y":
                                              print("Your recommended board game is: Jenga (Check out the DK Editon!)")
                                          elif strHands == "n":
                                              print("Your recommended board game is: Taboo")
                          elif strParty == "n":
                              strKnowItAll = input("Are you a know-it-all? (y/n) \n")
                              if strKnowItAll == "y":
                                  print("Your recommended board game is: Trivial Persuit")
                              elif strKnowItAll == "n":
                                  strAs = input("Do you get straight-A's? (y\n) \n")
                                  if strAs == "y":
                                      print("Your recommended board game is: Scrabble")
                                  elif strAs == "n":
                                      strTrains = input("Do you like Trains? (y/n) \n")
                                      if strTrains == "y":
                                          strEcon = input("Do you like games about Economics? (y/n) \n")
                                          if strEcon == "y":
                                              print("Your recommended board game is: Steam")
                                          elif strEcon == "n":
                                              print("Your recommended board game is: Ticket to Ride")
                                      elif strTrains == "n":
                                          strSimpRules = input("Simple or Complex rules? (simple/complex) \n")
                                          if strSimpRules == "simple":
                                              strWordsTiles = input("Words or Tiles? (words/tiles) \n")
                                              if strWordsTiles == "words":
                                                  print("Your recommended board game is: Scattergories")
                                              elif strWordsTiles == "tiles":
                                                  print("Your recommended board game is: Qwirkle")
                                          elif strSimpRules == "complex":
                                              strHardChoices = input("Want constant hard choices? (y/n) \n")
                                              if strHardChoices == "y":
                                                  strFarming = input("Would you like a game about farming? (y/n) \n")
                                                  if strFarming == "y":
                                                      print("Your recommended board game is: Agricola")
                                                  elif strFarming == "n":
                                                      strTwoGames = input("Would you mind having to buy two games? (y/n)")
                                                      if strTwoGames == "y":
                                                          strGeeks = input("Are all players serious board game geeks? (y/n) \n")
                                                          if strGeeks == "y":
                                                              print("Your recommended board game is: Puerto Rico")
                                                          elif strGeeks == "n":
                                                              print("Your recommended board game is: Domaine")
                                                      elif strTwoGames == "n":
                                                          print("Your recommended board games are: 'Cities' or 'Knights'")
                                              elif strHardChoices == "n":
                                                  strDeck = input("Would you like a Card/Deck based game? (y/n) \n")
                                                  if strDeck == "y":
                                                      strComplex = input("Do you prefer More or Less game complexity? (more/less) \n")
                                                      if strComplex == "more":
                                                          print("Your recommended board game is: 7 Wonders")
                                                      elif strComplex == "less":
                                                          print("Your recommended board game is: Dominion")
                                                  elif strDeck == "n":
                                                      strPlan = input("Do you like to plan your strategy before your turn? (y/n) \n")
                                                      if strPlan == "y":
                                                          print("Your recommended board game is: Settlers of Catan")
                                                      elif strPlan == "n":
                                                          strTurns = input("Defined Turns or No Downtime? (defined turns/no downtime) \n")
                                                          if strTurns == "defined turns":
                                                              print("Your recommended board game is: Carcassonne")
                                                          elif strTurns == "no downtime":
                                                              print("Your recommended board game is: Pillars of the Earth")


# END IFs
print()
strEnd = input("Press ENTER to exit. ")

