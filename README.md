# credit-app-notification
Micro Service to handle notification for the credit app

This service takes in a notification and dispatches it via the set type destination.

### Examples
#### SMS
```
{
    NotificationRecipient: "+44700939393",
    NotificationType: SMS,
    NotiricationSubject: "",
    NiotificationMessage: "Hello Dear Moses".
}
```

##### EMail
```
{
    NotificationRecipient: "sampleemail@email.com",
    NotificationType: EMAIL,
    NotiricationSubject: "Re: Free this weekend?",
    NiotificationMessage: "Hello Dear Moses".
}
```
