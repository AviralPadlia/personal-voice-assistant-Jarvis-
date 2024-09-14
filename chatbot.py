import random
import re
import responses

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = False

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word in user_message:
            has_required_words = True
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response(random.choice(responses.greeting), responses.greeting, single_response=True)
    response(random.choice(responses.bye), ['bye', 'goodbye',"tata"], single_response=True)
    response(random.choice(responses.good)+" how can I help you",['i','am','doing','good','fine','great','well','amazing'], single_response=True)
    response(random.choice(responses.howareyou), ['how','are', 'you'], required_words=['how'])
    response(random.choice(responses.welcome), ['thank', 'thanks'], single_response=True)
    response(random.choice(responses.thankyou), ['good','great','awesome','amazing'],required_words=['you'])
    response(random.choice(responses.mad),['are' ,'you','mad'],required_words=['mad'])
    response(random.choice(responses.love),["i","love","you"],required_words=['love'])
    response(random.choice(responses.complement),["compliment","me"],required_words=["compliment"])
    response(random.choice(responses.pickupLine),["say","tell","pick","up","line"],required_words=["pick","up","line"])
    response(random.choice(responses.marryme),["can","you","marry","me","i","want","to"], required_words=['marry'])
    response(random.choice(responses.hug),["hug","can","we"], required_words=['hug'])
    response(random.choice(responses.roast),["roast","me"], required_words=['roast'])
    response(random.choice(responses.sleep),["do","you","sleep","like","sleeping"], required_words=['sleep'])
    response(random.choice(responses.name),["who","are","you","what","your","name"], required_words=["name",'who'])
    response(random.choice(responses.single),["are","you","single"], required_words=['single'])
    response(random.choice(responses.features),["what","can","you","do","how","can","you","help","me"], required_words=['help'])
    response(responses.miss,['i' ,'you','miss','missed','missing'],required_words=['miss','missed','missing'])
    response(responses.doLove,["Do","you","love","me"], required_words=["love"])
    response(responses.age,["how","what","birthday","old","age"], required_words=["age","birth","old"])
    response(responses.gf,["who","need","can","find","me","girl","friend","girlfriend"], required_words=['girl','girlfriend'])
    response(responses.eat,["do","you","eat","what","eating","ate"], required_words=['eat','ate','eating'])
    response(responses.srcCode,["what","is","source","code"], required_words=['source','code'])
    response(responses.human,["are","you","human","bot"], required_words=['human','bot'])
    response(responses.hairs,["do","you","have","hair","hairs"], required_words=['hairs'])
  

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return "Sorry! I didn't get it" if highest_prob_list[best_match] < 5 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response