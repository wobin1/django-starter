from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer



class User(APIView):

    def get(self, request):
        # geting all data from the database
        try:
            user = CustomUser.objects.all()
            serializer = UserSerializer(user, many=True)
            print(serializer)
            return Response({"status": "success", "message": 
                                "Users gotten successfully", 
                                "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e))

    
    def post(self, request):    
        request_data = request.data
        print(request_data)

        # serializes request data and save new user
        try:
            serializer = UserSerializer(data=request_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            print("user saved")
            return Response({"status": "success", 
                                "message": "user created sucessfully",
                                "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"printing exception {e}")
            return Response({"message": str(e)})


    
        # checking if user is in database
        user = CustomUser.objects.get(pk=id)

        user.delete()

        return Response({"message": "user deleted!!"})


class SingleUser(APIView):

    def put(self, request, id):
        # getting post data
        request_data = request.data

        # checking if user is in database
        user = CustomUser.objects.get(pk=id)
        print("user valid!!!")

        # saving post data to database
        serializer = UserSerializer(user, data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        print("user saved!!!")
        
        return Response({"status": "success", "message": "User updated!", "data": serializer.data})
    
    
    def delete(self, request, id):
        # checking if user is in database
        user = CustomUser.objects.get(pk=id)

        user.delete()

        return Response({"message": "user deleted!!"})

