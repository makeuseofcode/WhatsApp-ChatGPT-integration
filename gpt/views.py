from rest_framework.response import Response
import openai
from rest_framework.views import APIView

class OpenAIGPTView(APIView):

    def get(self, request):
        input = request.GET.get('q')
        openai.api_key = "ENTER_OPENAI_KEY"
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": input}]
        )
        answer = completion['choices'][0]['message']['content']
        return Response(answer)
