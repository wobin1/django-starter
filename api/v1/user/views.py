from django.shortcuts import render
from django.http import HttpResponse



class UserList(APIView):

    def get(self, request):
        # geting all data from the database
        try:
            user = CustomUser.objects.all()
            serializer = UserSerializer(user, many=True)
            print(serializer)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=400)


class UserCreate(APIView):
    # create user function
    def post(self, request):    
        request_data = request.data
        print(request_data)

        # serializes request data and save new user
        try:
            serializer = UserSerializer(data=request_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            print("user saved")
            return Response({"message": str(e)}, status=200)
        except Exception as e:
            print(f"printing exception {e}")
            return Response({"message": str(e)}, status=400)

    