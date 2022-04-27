from lib2to3.pgen2.token import OP
import json


class BlackJack:

    player = ''
    opponent = ''
    player_cards = []
    opponent_cards = []
    player_score = 0
    opponent_core = 0

    def __init__(self, Player, Opponent):
        self.player = Player
        self.opponent = Opponent

    def get_player(self):
        return self.player

    
    def set_player(self, Player):
        self.player = Player


    def get_opponent(self):
        return self.opponent

    
    def set_opponent(self, Opponent):
        self.opponent = Opponent
    

    def get_player_cards(self):
        return self.player_cards

    
    def set_player_cards(self, Cards):
        data = self.player_cards
        try:
            if isinstance(Cards,list):
                for elem in Cards:
                    data.append(elem)
            elif isinstance(Cards,str):
                data.append(Cards)
        except:
            print("Error in set_player_cards method")
            

    def get_opponent_cards(self):
        return self.opponent_cards

    
    def set_opponent_cards(self, Cards):
        data = self.opponent_cards
        try:
            if isinstance(Cards,list):
                for elem in Cards:
                    data.append(elem)
            elif isinstance(Cards,str):
                data.append(Cards)
        except:
            print("Error in set_opponent_cards method")

    
    def get_player_score(self):
        return self.player_score

    def convert_player_cards_to_score(self, all_cards):
        arr_data = self.player_cards
        score = self.player_score
        for card in arr_data:
            score+=all_cards[card]
        self.player_score = score


    def get_opponent_score(self):
        return self.opponent_score

    def convert_opponent_cards_to_score(self, all_cards):
        arr_data = self.opponent_cards
        score = self.opponent_score
        for card in arr_data:
            score+=all_cards[card]
        self.opponent_score = score


    def read_all_cards():
        with open('json_data.json') as json_file:
            data = json.load(json_file)        
        return data

    
    

        
    
