import urllib, urllib.request, urllib.parse


class SendSms:
    def __init__(
        self,
        message="""
        Hi Ikram,

        A new service request has been assigned to you for the I.T department located on Mezzanine Floor. The requester's name is Aasif, phone number  9975163969, extension 33033. The ticket number for this request is 1.

        The reported problem is: Dick is not working

        Kokilaben Hospital.

        """,
        number="8767861216,9004579961,8080513540",
    ):
        url = "http://www.smscountry.com/smscwebservice_bulk.aspx"
        values = {
            "user": "kdah",
            "passwd": "kdah@1234",
            "message": message,
            "mobilenumber": number,
            "mtype": "N",
            "SID": "KDAHOS",
            "DR": "Y",
        }
        data = urllib.parse.urlencode(values)
        data = data.encode("utf-8")
        request = urllib.request.Request(url, data)
        # print(request.data)
        response = urllib.request.urlopen(request)
        # print (response.read().decode('utf-8'))


default_message = """
Hi {technician_name},

A new service request has been assigned to you for the {department} department located on {floor}. The requester's name is {requester_name}, phone number  {phone_number}, extension {extension}. The ticket number for this request is {ticket_id}.

The reported problem is: {problem}


Kokilaben Hospital.

"""

number = "8767861216"

if __name__ == "__main__":
    test = SendSms(default_message, number)
    print(test)
