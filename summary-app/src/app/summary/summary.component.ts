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
  summary: any;
  emailSummary: string = '';
  slackSummary: string = '';

  constructor(private summaryService: SummaryService) { }

  onSubmit(): void {
    this.summaryService.getSummary(this.tokens, this.hours).subscribe(
      data => {
        this.summary = data;
        this.emailSummary = data.email_summary;
        this.slackSummary = data.slack_summary;
      },
      error => console.error(error)
    );
  }
}