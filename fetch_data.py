import requests

def get_hotel_metrics():
    url = "https://zjmuqawoq5azfcndh7jjlrmroa.appsync-api.ap-south-1.amazonaws.com/graphql"

    headers = {
        "Authorization": "Bearer eyJraWQiOiJZbHpQeHFMNWtFVVwvSEx6UWhDVU04bDUwQXpERDRFZnlcL0dhd0hTWVpkK1E9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIxZWRlYTExOS0zM2U5LTQ5NjItOWJhZS0yMWQzOGU4Y2Q4YjAiLCJjdXN0b206cm9sZXMiOiJbXSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGgtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aC0xX2JrakdPQ0tFYSIsInBob25lX251bWJlcl92ZXJpZmllZCI6ZmFsc2UsImNvZ25pdG86dXNlcm5hbWUiOiIxZWRlYTExOS0zM2U5LTQ5NjItOWJhZS0yMWQzOGU4Y2Q4YjAiLCJjdXN0b206bWV0YV9kYXRhIjoie1wiZ3JvdXBJZFwiOlwiXCIsXCJicmFuZElkXCI6XCJcIixcImhvdGVsSWRcIjpcIlwiLFwiZGVwYXJ0bWVudElkXCI6XCJcIixcInJvbGVcIjpcIlN1cGVyIEFkbWluXCIsXCJyZXN0YXVyYW50SWRcIjpcIlwiLFwidXNlcklkXCI6XCIxZWRlYTExOS0zM2U5LTQ5NjItOWJhZS0yMWQzOGU4Y2Q4YjBcIixcImVtYWlsX3ZlcmlmaWVkXCI6dHJ1ZSxcImVtYWlsXCI6XCJzdXBlcmFkbWluQGh1ZGluaS5pb1wiLFwiZ2l2ZW5fbmFtZVwiOlwiU3lzdGVtXCIsXCJmYW1pbHlfbmFtZVwiOlwiVXNlclwifSIsImdpdmVuX25hbWUiOiJTeXN0ZW0iLCJvcmlnaW5fanRpIjoiNmFjMTU0YTctMTEyZC00NjY3LWE3ZDYtZjZiMjhiNGE2MWMyIiwiYXVkIjoiNWU2ZHYzcHUwZ281ZjVmcDVocDQxc2czZWQiLCJldmVudF9pZCI6IjViYjAwYWNkLTdiMzctNDgxMS05ZDliLTk1YjY3ZTNkMGE5YSIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNzUyMDM1MjI5LCJjdXN0b206c3RhdHVzIjoiYWN0aXZlIiwiZXhwIjoxNzUyMDM5OTk4LCJjdXN0b206cGVybWlzc2lvbnMiOiJ7XCJncm91cHNcIjoyLFwiYnJhbmRzXCI6MixcImhvdGVsc1wiOjIsXCJkZXZpY2VSZWdpc3RyYXRpb25cIjoyLFwicmVzdGF1cmFudFwiOjIsXCJzcGFcIjoyLFwicm9vbXNcIjoyLFwibGFuZ3VhZ2VDb25maWdcIjoyLFwibm90aWZpY2F0aW9uQ29uZmlnXCI6MixcInBlcm1pc3Npb25zXCI6MixcInJvbGVzXCI6MixcImFjY291bnRzXCI6MixcImluUm9vbURpbmluZ1wiOjIsXCJob3VzZUtlZXBpbmdcIjoyLFwiZGVwbG95bWVudENvbmZpZ1wiOjIsXCJjaXR5R3VpZGVcIjoyLFwib2ZmZXJzXCI6MixcImFtZW5pdGllc1wiOjIsXCJhY2NvbW1vZGF0aW9uc1wiOjIsXCJsb3lhbHR5XCI6MixcInJlZGlyZWN0VXJsXCI6MixcImZlZWRiYWNrXCI6MixcImVtYWlsQ29uZmlndXJhdGlvblwiOjIsXCJ0dkNoYW5uZWxzXCI6MixcInJlcG9ydHNcIjoyLFwibG9jYXRpb25cIjoyLFwiaG90ZWxTeXN0ZW1zXCI6MixcInZlbmRvckNvbmZpZ1wiOjIsXCJkZXNpZ25Db25maWdzXCI6MixcInVzZXJzXCI6MixcInNlcnZpY2VSZXF1ZXN0XCI6MixcIm5vdGlmaWNhdGlvbnNcIjoyLFwidGVsZXBob255XCI6MixcIm9yZGVyVHJhbnNhY3Rpb25cIjoyLFwicmVzdGF1cmFudERhc2hib2FyZFwiOjIsXCJzcGFEYXNoYm9hcmRcIjoyLFwiYWNjb21tb2RhdGlvbkRhc2hib2FyZFwiOjIsXCJpblJvb21EaW5pbmdEYXNoYm9hcmRcIjoyLFwic2VydmljZVJlcXVlc3REYXNoYm9hcmRcIjoyLFwiZGV2aWNlTW9uaXRvcmluZ1wiOjIsXCJmQW5kQkRhc2hib2FyZFwiOjIsXCJhbmFseXRpY3NcIjoyLFwiYXBwVXNhZ2VSZXBvcnRcIjoyLFwicmVzdGF1cmFudFJlcG9ydFwiOjIsXCJpblJvb21EaW5pbmdSZXBvcnRcIjoyLFwiaG91c2VLZWVwaW5nUmVwb3J0XCI6MixcInNwYVJlcG9ydFwiOjIsXCJkaWdpdGFsQ2hlY2tJblJlcG9ydFwiOjIsXCJhY3Rpdml0eVwiOjIsXCJwYXltZW50c1wiOjAsXCJhcHBDb25maWd1cmF0aW9uc1wiOjIsXCJjb252ZXJzYXRpb25zXCI6MCxcImNhbm5lZE1lc3NhZ2VzXCI6MCxcIndlbGNvbWVNZXNzYWdlXCI6MH0iLCJjdXN0b206cm9sZSI6IlNVUEVSX0FETUlOIiwiY3VzdG9tOnVzZXJfdHlwZSI6ImNtcyIsImlhdCI6MTc1MjAzOTY5OCwiZmFtaWx5X25hbWUiOiJVc2VyIiwianRpIjoiYzI5MzI3YTAtNGE2YS00YTIyLThhNzUtYTg3OTE1MjFhNjk0IiwiZW1haWwiOiJzdXBlcmFkbWluQGh1ZGluaS5pbyJ9.faFyTxITd2PgKukoaw8gyvDnI40WEgsZkc_qTwQtxASQBpkVqo-i_CFPeLm71eU02zVIjt01Tj4O6cYIpHe67Z2uqDYPGBaJIGc0AXkE1rDR5J-JnMFOBkU3NQ68RjGpFiTZ-NIVziqZCUDTTFDlr6S6VyJAzMjF1WUvVTBwTfvsHPMVJa8nAMCzTF-JLFgUm6HyFk2JOIRcU9pASFcdq4FXFtnphkmiw6_R0g_aP-n8RisCfPKgRI9V2I4mXPEUqKP2j4UoC4yqeDfSyfQg9SBSdLWRLgfQanP55FY8d36RRYpT5PmptDZUNIXQ7b2fjIgSI3inh8iLOUVpOKpnZQ",
      
        "Content-Type": "application/json"
    }

    query = """ 
    query MyQuery {
  getHotelMetrics(

hotelId: "02497a43-5339-453a-9731-d14431a66070"
    endDate:
"2025-07-02"
    fetchFromPostgres: true
    startDate:
"2025-04-28"
  ) {
    hotelMetric {
		day

formattedDate
      hotelId
      hotelName

reportDate
      channelCheckInBreakDown {
        iptv

  kiosk
        mobileApp
        pwa

staffConnect
        tablet
      }
      channelWiseStats
{
        iptv {
          activityBooking {

failed
            success
          }

adoptionRate
          adoptionByCompletedAction {

addGuest
            checkIn
            emailTrigger

    eregistration
            idVerification

payment
            personalisation_updatereservation

 preCheckIn
            pushDocument
			assignRoom
		
	roomStatus
          }
          averageCheckInTime

  checkInDropOffs {
            checkInStart

finalCheckIn
            keyGeneration

preCheckInSteps
          }
          checkIns {

success
            failed
          }
          checkOuts
{
            failed
            success
          }

    conversionRate
          eRegistrations {

failed
            success
          }

emailsSent
          emailsClicked
          engagementRate

        errorRate
          houseKeeping {
            counts
{
              failed
              success

}
            revenue
          }
          idVerifications
{
            failed
            success
          }

    ird {
            counts {
              failed

    success
            }
            revenue
          }

         payments {
            failed
            success

       }
          preCheckIns {
            failed

  success
          }
          profileUpdations {

 failed
            success
          }
          restaurant
{
            counts {
              failed

success
            }
            revenue
          }

     spa {
            counts {
              success

      failed
            }
            revenue

}
          upsell {
            counts {

failed
              success
            }

revenue
          }
          upsellConversionRate

}
        kiosk {
          activityBooking {

failed
            success
          }

adoptionRate
          adoptionByCompletedAction {

addGuest
            checkIn
            emailTrigger

    eregistration
            idVerification

payment
            personalisation_updatereservation

 preCheckIn
            pushDocument
			assignRoom
		
	roomStatus
          }
          averageCheckInTime

  checkIns {
            failed
            success

}
          checkInDropOffs {
            checkInStart

     finalCheckIn
            keyGeneration

preCheckInSteps
          }
          checkOuts {

failed
            success
          }

eRegistrations {
            failed
            success

    }
          conversionRate
          emailsClicked

   emailsSent
          engagementRate
          errorRate

       houseKeeping {
            counts {

failed
              success
            }

revenue
          }
          idVerifications {

failed
            success
          }
          ird {

        counts {
              failed
              success

          }
            revenue
          }

payments {
            failed
            success

}
          preCheckIns {
            failed

success
          }
          profileUpdations {

failed
            success
          }
          restaurant
{
            counts {
              failed

success
            }
            revenue
          }

     spa {
            counts {
              failed

     success
            }
            revenue

}
          upsell {
            counts {

failed
              success
            }

revenue
          }
          upsellConversionRate

}
        mobileApp {
          activityBooking {

failed
            success
          }

adoptionRate
          adoptionByCompletedAction {

addGuest
            checkIn
            emailTrigger

    eregistration
            idVerification

payment
            personalisation_updatereservation

 preCheckIn
            pushDocument
			assignRoom
		
	roomStatus
          }
          averageCheckInTime

  checkInDropOffs {
            checkInStart

keyGeneration
            finalCheckIn

preCheckInSteps
          }
          checkIns {

success
            failed
          }
          checkOuts
{
            success
            failed
          }

    conversionRate
          eRegistrations {

success
            failed
          }

emailsClicked
          emailsSent
          engagementRate

        errorRate
          houseKeeping {
            counts
{
              failed
              success

}
            revenue
          }
          idVerifications
{
            failed
            success
          }

    ird {
            counts {
              failed

    success
            }
            revenue
          }

         payments {
            failed
            success

       }
          preCheckIns {
            failed

  success
          }
          profileUpdations {

 failed
            success
          }
          restaurant
{
            counts {
              failed

success
            }
            revenue
          }

     spa {
            counts {
              failed

     success
            }
            revenue

}
          upsell {
            counts {

failed
              success
            }

revenue
          }
          upsellConversionRate

}
        pwa {
          activityBooking {

failed
            success
          }

adoptionRate
          averageCheckInTime

adoptionByCompletedAction {
            addGuest

checkIn
            emailTrigger
            eregistration

         idVerification
            payment

personalisation_updatereservation
            preCheckIn

    pushDocument
			assignRoom
		  	roomStatus

 }
          checkInDropOffs {
            finalCheckIn

      checkInStart
            keyGeneration

preCheckInSteps
          }
          checkIns {

failed
            success
          }
          checkOuts
{
            failed
            success
          }

    conversionRate
          eRegistrations {

failed
            success
          }

emailsClicked
          emailsSent
          engagementRate

        errorRate
          houseKeeping {
            counts
{
              success
              failed

}
            revenue
          }
          idVerifications
{
            failed
            success
          }

    ird {
            counts {
              failed

    success
            }
            revenue
          }

         payments {
            failed
            success

       }
          preCheckIns {
            failed

  success
          }
          profileUpdations {

 failed
            success
          }
          restaurant
{
            counts {
              failed

success
            }
            revenue
          }

     spa {
            revenue
            counts {

    failed
              success
            }

}
          upsell {
            counts {

failed
              success
            }

revenue
          }
          upsellConversionRate

}
        staffConnect {
          activityBooking {

   failed
            success
          }

adoptionRate
          adoptionByCompletedAction {

addGuest
            emailTrigger
            checkIn

    eregistration
            idVerification

payment
            personalisation_updatereservation

 preCheckIn
            pushDocument
			assignRoom
		
	roomStatus
          }
          averageCheckInTime

  checkInDropOffs {
            finalCheckIn

keyGeneration
            checkInStart

preCheckInSteps
          }
          checkIns {

failed
            success
          }
          checkOuts
{
            failed
            success
          }

    conversionRate
          eRegistrations {

failed
            success
          }

emailsClicked
          emailsSent
          engagementRate

        errorRate
          houseKeeping {
            counts
{
              failed
              success

}
            revenue
          }
          idVerifications
{
            success
            failed
          }

    ird {
            revenue
            counts {

   failed
              success
            }
          }

         payments {
            failed
            success

       }
          preCheckIns {
            failed

  success
          }
          profileUpdations {

 failed
            success
          }
          restaurant
{
            counts {
              success

failed
            }
            revenue
          }

    spa {
            counts {
              failed

    success
            }
            revenue
          }

         upsell {
            counts {
              failed

            success
            }
            revenue

  }
          upsellConversionRate
        }
        tablet
{
          activityBooking {
            failed

success
          }
          adoptionRate

adoptionByCompletedAction {
            addGuest

checkIn
            eregistration
            emailTrigger

         idVerification
            payment

personalisation_updatereservation
            preCheckIn

    pushDocument
			assignRoom
		  	roomStatus

 }
          averageCheckInTime
          checkInDropOffs {

          checkInStart
            finalCheckIn

keyGeneration
            preCheckInSteps
          }

  checkOuts {
            failed
            success

 }
          checkIns {
            failed

success
          }
          conversionRate

emailsSent
          eRegistrations {
            failed

       success
          }
          emailsClicked

engagementRate
          errorRate
          houseKeeping {

          counts {
              failed

success
            }
            revenue
          }

     idVerifications {
            failed

success
          }
          ird {
            counts {

            failed
              success
            }

     revenue
          }
          payments {

failed
            success
          }

profileUpdations {
            failed
            success

      }
          preCheckIns {
            failed

 success
          }
          restaurant {

counts {
              failed
              success

  }
            revenue
          }
          spa {

     counts {
              failed
              success

       }
            revenue
          }
          upsell
{
            counts {
              failed

success
            }
            revenue
          }

     upsellConversionRate
        }
      }
      totalStats
{
        activityBooking {
          failed

success
        }
        adoptionRate

adoptionByCompletedAction {
          addGuest

checkIn
          emailTrigger
          eregistration

   idVerification
          payment

personalisation_updatereservation
          preCheckIn

pushDocument
		  assignRoom
		  roomStatus
        }

      averageCheckInTime
        checkInDropOffs {

checkInStart
          finalCheckIn

preCheckInSteps
          keyGeneration
        }

checkIns {
          failed
          success
        }

     conversionRate
        checkOuts {
          failed

     success
        }
        eRegistrations {

failed
          success
        }
        emailsSent

   emailsClicked
        engagementRate
        errorRate

    houseKeeping {
          counts {
            failed

       success
          }
          revenue
        }

    idVerifications {
          failed
          success

   }
        ird {
          counts {
            failed

          success
          }
          revenue
        }

       payments {
          failed
          success

}
        preCheckIns {
          success

failed
        }
        profileUpdations {

failed
          success
        }
        restaurant {

       counts {
            success
            failed

   }
          revenue
        }
        spa {

counts {
            failed
            success

}
          revenue
        }
        upsell {

counts {
            failed
            success

}
          revenue
        }

upsellConversionRate
      }
    }
    }

}
    """

    payload = {
        "query": query,
        "variables": {}
    }

    response = requests.post(url, json=payload, headers=headers)

    print("STATUS:", response.status_code)
    print("BODY:", response.text)

    response.raise_for_status()
    return response.json()
