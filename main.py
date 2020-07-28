import Command
import Echo


if __name__ == "__main__":
    args = Command.paramDecode()
    send_mail = args.email
    From = args.From
    password = args.password
    print("send_mail:%s\nFrom:%s\n" % (send_mail, From))
    Echo.echo(send_mail, password, From)
