import { Component, OnInit } from '@angular/core';
import { CommunicationService } from 'src/app/services/communication.service';
import { ChartDataSets, ChartOptions, ChartType } from 'chart.js';
import { Color, Label } from 'ng2-charts';

@Component({
  selector: 'app-crypto-chart',
  templateUrl: './crypto-chart.component.html',
  styleUrls: ['./crypto-chart.component.scss']
})
export class CryptoChartComponent implements OnInit {

  coins:string[] = ['BTC', 'ETH']
  selectedCoin = 'BTC';
  times = [1, 4];
  selectedTime = 1;

  apiChartData: any;

  chartData: ChartDataSets[] = [
    { data: [], label: 'Crypto Price USD' },
  ];

  chartLabels: Label[] = [];


  chartOptions = {
    responsive: true,
  };

  chartColors: Color[] = [
    {
      borderColor: 'RGB(3, 160, 98)',
      backgroundColor: 'RGBA(3, 160, 98, 0.3)',
    },
  ];

  chartLegend = true;
  chartPlugins = [];
  chartType: ChartType = 'line';

  constructor(private comm: CommunicationService) { }

  ngOnInit(): void {
    this.getChartData();
  }

  getChartData() {
    this.chartData[0].data = [];
    this.chartLabels = [];
    this.comm.getChartData(this.selectedCoin, 1, 1, this.selectedTime)
      .subscribe(data => {
        this.apiChartData = data;
        this.setChartData()});
  }

  setChartData() {
    let date: Date;
    for(const data of this.apiChartData) {
      this.chartData[0].data?.push(data.close);
      date = new Date(data.time*1000);
      this.chartLabels.push(date.toLocaleTimeString());
    }
  }

  coinSelection(event: any) {
    this.selectedCoin = event.value;
    this.getChartData();
  }

  timeSelection(event: any) {
    this.selectedTime = event.value
    this.getChartData()
  }

}
