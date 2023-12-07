import { Component, OnInit } from '@angular/core';
declare var $: any;

@Component({
  selector: 'app-criar-votacao',
  templateUrl: './criar-votacao.component.html',
  styleUrls: ['./criar-votacao.component.css']
})

export class CriarVotacaoComponent implements OnInit {
  public loading = false;

  listaOpcao: string[] = [];

  constructor() { }

  ngOnInit() {
  }

  addOpcao(input){
    this.listaOpcao.push(input.value);
    input.value = "";
  }

  removeOpcao(index){
    this.listaOpcao.splice(index, 1);
  }

}
