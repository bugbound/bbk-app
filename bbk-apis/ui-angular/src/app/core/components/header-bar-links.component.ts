import { Component } from '@angular/core';

@Component({
  selector: 'app-header-bar-links',
  template: `
    <div class="navbar-menu">
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <a href="https://github.com/bugbound/bbk-app" target="_blank" rel="noopener noreferrer">
              <i class="fab fa-github fa-2x" aria-hidden="true"></i>
            </a>
          </div>
        </div>
      </div>
    </div>
  `,
  styles: [
    `
      :host {
        width: 100%;
      }
    `
  ]
})
export class HeaderBarLinksComponent {}
