import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'splitto';
  constructor(
    private router:Router
    ){}

  ngOnInit(){
    if(localStorage.getItem('username')===null){
      this.router.navigate(['/login']);
    }
  }
}
