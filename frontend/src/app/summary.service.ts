import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SummaryService {

  private slackSummaryUrl = 'http://127.0.0.1:5000/slack-summary';
  private emailSummaryUrl = 'http://127.0.0.1:5000/email-summary';
  private draftResponseEmailsUrl = 'http://127.0.0.1:5000/draft-response-emails';

  constructor(private http: HttpClient) { }

  getSlackSummary(tokens: any, hours: number): Observable<any> {
    return this.http.post<any>(this.slackSummaryUrl, {
      SLACK_USER_TOKEN: tokens.slackUserToken,
      SLACK_USER_ID: tokens.slackUserId,
      hours: hours
    });
  }

  getEmailSummary(tokens: any, hours: number): Observable<any> {
    return this.http.post<any>(this.emailSummaryUrl, {
      GOOGLE_CLIENT_ID: tokens.googleClientId,
      GOOGLE_CLIENT_SECRET: tokens.googleClientSecret,
      GOOGLE_REFRESH_TOKEN: tokens.googleRefreshToken,
      hours: hours
    });
  }

  draftResponseEmails(tokens: any, hours: number): Observable<any> {
    return this.http.post<any>(this.draftResponseEmailsUrl, {
      GOOGLE_CLIENT_ID: tokens.googleClientId,
      GOOGLE_CLIENT_SECRET: tokens.googleClientSecret,
      GOOGLE_REFRESH_TOKEN: tokens.googleRefreshToken,
      hours: hours
    });
  }
}
