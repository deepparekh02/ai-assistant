import { Component } from '@angular/core';
import { CommonModule, NgFor, NgIf } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { SummaryService } from '../summary.service';
import { MarkdownModule } from 'ngx-markdown';

@Component({
  selector: 'app-summary',
  standalone: true,
  imports: [CommonModule, FormsModule, NgFor, NgIf, MarkdownModule],
  templateUrl: './summary.component.html',
  styleUrls: ['./summary.component.css']
})
export class SummaryComponent {
  tokens = {
    googleClientId: '',
    googleClientSecret: '',
    googleRefreshToken: '',
    slackUserToken: '',
    slackUserId: ''
  };
  hours: number = 24;
  emailSummary: string = '';
  slackSummary: string = '';
  draftSummary: any;
  draftMessage: string = '';

  constructor(private summaryService: SummaryService) { }

  getEmailSummary(): void {
    this.summaryService.getEmailSummary(this.tokens, this.hours).subscribe(
      data => this.emailSummary = data.email_summary,
      error => console.error(error)
    );
  }

  getSlackSummary(): void {
    this.summaryService.getSlackSummary(this.tokens, this.hours).subscribe(
      data => this.slackSummary = data.slack_summary,
      error => console.error(error)
    );
  }

  draftResponseEmails(): void {
    this.summaryService.draftResponseEmails(this.tokens, this.hours).subscribe(
      data => {
        this.draftMessage = data.message;
        this.draftSummary = data.drafts;
      },
      error => console.error(error)
    );
  }
}