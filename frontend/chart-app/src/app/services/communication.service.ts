import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CommunicationService {

  constructor(private http: HttpClient) { }

  getChartData(coin='BTC', durationSelection=1, durationType=1, duration=1) {
    const url =
      `http://localhost:8000/api/graph/?coin=${coin}&durationSelection=${durationSelection}&durationType=${durationType}&duration=${duration}`;
    return this.http.get(url);
  }
}
