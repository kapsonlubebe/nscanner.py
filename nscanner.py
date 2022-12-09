import scapy.all as scapy
import optparse

def userInput():

    parse = optparse.OptionParser()
    parse.add_option("-i" , "--ipaddress", dest = "ipAddress" , help = "Enter IP Address")
    (userInput, arguments) = parse.parse_a rgs()

    if not userInput.ipAddress:
        print("Enter aa IP Address")

    return userInput

def scanning(ip):
    arpRequest = scapy.ARP(pdst = ip)
    broadcastPacket = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    combinedPack = broadcastPacket/arpRequest
    (answeredList , unansweredList) = scapy.srp(combinedPack,timeout=1)
    answeredList.summary()

userIpAdress = userInput()
scanning(userIpAdress.ipAddress)
