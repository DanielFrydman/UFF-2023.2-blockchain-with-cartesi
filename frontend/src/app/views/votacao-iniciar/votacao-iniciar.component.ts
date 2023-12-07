import { Component, OnInit } from '@angular/core';
declare var $: any;

@Component({
  selector: 'app-votacao-iniciar',
  templateUrl: './votacao-iniciar.component.html',
  styleUrls: ['./votacao-iniciar.component.css']
})

export class VotacaoIniciarComponent implements OnInit {
  public loading = false;

  constructor() { }

  ngOnInit() {
  }

}
