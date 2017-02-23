require(mailR)

send_text <- function(msg = "no message input",
                      number="YOUR NUMBER HERE",
                      sp="B")
{

      ## Build carrier dataframe.
      carriers <- data.frame(Carrier = c("B", "R", "T", "V"),
                             Tail = c(
                                 "@txt.bell.ca",
                                 "@pcs.rogers.com",
                                 "@msg.telus.com",
                                 "@vmobile.ca"
                                 ))

      # Source appropriate carrier email extension.
      tail <- as.character(carriers[carriers$Carrier == sp, 2])

      # Send message using mailR function.
      send.mail(from = Sys.getenv('GMAIL'),
                to = paste(number, tail, sep=""),
                subject = "",
                body = msg,
                smtp = list(
                    host.name = "smtp.gmail.com",
                    port = 465,
                    user.name = Sys.getenv('GMAIL'),
                            passwd= Sys.getenv('GMAIL_PW'),
                            ssl=TRUE),
                authenticate = TRUE,
                send = TRUE)
      }

args <- commandArgs(trailingOnly = TRUE)

send_text(
    paste("The similarity was below ", args[1], "%!"),
    number = Sys.getenv('K_PHONE'),
    sp="V"
)

print("SENT!")
