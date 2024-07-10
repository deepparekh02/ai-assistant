import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SummaryService {

  private apiUrl = 'http://127.0.0.1:5000/summary'; // Adjust the URL as per your backend

  constructor(private http: HttpClient) { }

  getSummary(tokens: any, hours: number): Observable<any> {
    return this.http.post<any>(this.apiUrl, { 
      GOOGLE_CLIENT_ID: tokens.googleClientId,
      GOOGLE_CLIENT_SECRET: tokens.googleClientSecret,
      GOOGLE_REFRESH_TOKEN: tokens.googleRefreshToken,
      SLACK_USER_TOKEN: tokens.slackUserToken,
      SLACK_USER_ID: tokens.slackUserId,
      hours: hours 
    });
  }
}
