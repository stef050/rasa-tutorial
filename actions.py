# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_core_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from mongoDbCrud import MongoCrud

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_howdy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # print(tracker.latest_message)
        MongoCrud.insert()
        whatTheySaid = tracker.latest_message['text']
        print(whatTheySaid)

        dispatcher.utter_message("howdy partner!")

        return []
