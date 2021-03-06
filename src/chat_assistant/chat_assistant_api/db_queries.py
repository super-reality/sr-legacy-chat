from .models import  Intent, Channel, Assistant, IntentExamples, Response
from django.forms.models import model_to_dict


def get_all_intent_names(assistant_id):
    assistant_obj = Assistant.objects.filter(id=assistant_id).first()
    all_intents   = Intent.objects.filter(assistant_id=assistant_obj).values_list('intent_name', flat=True)
    return list(all_intents)


def get_all_intents_of_bot(assistant_id, sentence_type):
    assistant_obj = Assistant.objects.filter(id=assistant_id).first()
    all_intents   = Intent.objects.filter(assistant_id=assistant_obj).all()
    if sentence_type == "example":
        all_examples_with_intents = get_all_example_sentences_of_intent(all_intents)
        return all_examples_with_intents, assistant_obj.assistant_name
    elif sentence_type == "response":
        all_responses_with_intents = get_all_responses_of_intent(all_intents)
        return all_responses_with_intents, assistant_obj.assistant_name


def get_all_example_sentences_of_intent(intent_objs):
    all_intent_examples = IntentExamples.objects.filter(intent_id__in=intent_objs)
    intent_list = [model_to_dict(intent) for intent in intent_objs]
    intent_dict = {}
    for intent in intent_list:
        intent_dict.update({intent['intent_name']:[]}) 
    all_examples = []
    for _ex in all_intent_examples:
        example = model_to_dict(_ex)
        intent_name = next(item for item in intent_list if item['id'] == example['intent_id'])
        intent_dict[intent_name['intent_name']].append(example['example_sentence'])
    
    return intent_dict


def get_all_responses_of_intent(intent_objs):
    all_intent_examples = Response.objects.filter(intent_id__in=intent_objs)
    intent_list = [model_to_dict(intent) for intent in intent_objs]
    intent_dict = {}
    for intent in intent_list:
        intent_dict.update({intent['intent_name']:[]}) 
    all_examples = []
    for _ex in all_intent_examples:
        example = model_to_dict(_ex)
        intent_name = next(item for item in intent_list if item['id'] == example['intent_id'])
        intent_dict[intent_name['intent_name']].append(example['response_sentence'])
    
    return intent_dict

