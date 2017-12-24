$(document).ready(function() {
  
      $("#toTop").click(function() {
          $("html, body").animate({
              scrollTop: 0
          }, 1000);
      });
      //  code for Password Strength Meter
      jQuery(document).ready(function() {
          "use strict";
          var options = {};
          options.ui = {
              container: "#form",
              showVerdictsInsideProgressBar: true,
              viewports: {
                  progress: ".pwstrength_viewport_progress",
                  verdict: ".pwstrength_viewport_verdict"
              },
              progressBarExtraCssClasses: "progress-bar-striped active"
          };
          options.common = {
              debug: true,
              zxcvbn: true,
              zxcvbnTerms: ['samurai', 'shogun', 'bushido', 'daisho', 'seppuku'],
              userInputs: ['#id_username', '#id_email']
          };
          options.rules = {
              activated: {
                  wordTwoCharacterClasses: true,
                  wordRepetitions: true
              }
          };
          $('#id_password1').pwstrength(options);
      });
  });