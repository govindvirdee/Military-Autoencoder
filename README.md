<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!--
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
-->


<!-- PROJECT LOGO -->

          __  __ ___ _    ___ _____ _   _____   __      
         |  \/  |_ _| |  |_ _|_   _/_\ | _ \ \ / /      
         | |\/| || || |__ | |  | |/ _ \|   /\ V /       
    _  _ |_| _|_|___|____|___| |_/_/_\_\_|_\_|_|___ ___ 
   /_\| | | |_   _/ _ \| __| \| |/ __/ _ \|   \| __| _ \
  / _ \ |_| | | || (_) | _|| .` | (_| (_) | |) | _||   /
 /_/ \_\___/  |_| \___/|___|_|\_|\___\___/|___/|___|_|_\
                                                        


<br />
<div align="center">
  <a href="https://github.com/govindvirdee/Military-Autoencoder">
    <!-- <img src="images/logo.png" alt="Logo" width="80" height="80"> -->
  </a>

  <h3 align="center">Military Autoencoder</h3>

  <p align="center">
    Creating an AutoEncoder to identify anomalous attack signatures in the NSL-KDD dataset 
    <br />
    <a href="https://github.com/govindvirdee/Military-Autoencoder"><strong>Explore the docs »</strong></a>
    <br />

  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <a href="#about-the-dataset">About The Dataset</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#todo">To-do list</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!--[![Product Name Screen Shot][product-screenshot]](https://example.com)-->

This project focuses on developing a machine learning model for anomaly detection in cyber defense data. By analyzing network traffic data, the aim is to identify unusual patterns or anomalies that could indicate potential security threats, such as intrusions or system failures. The project leverages the NSL-KDD dataset, an improved version of the KDD Cup 99 dataset, a widely recognized benchmark in cybersecurity research.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## About The Dataset

This project utilizes the NSL-KDD dataset, an improved version of the widely known KDD Cup 99 dataset for network intrusion detection. The NSL-KDD dataset addresses some of the inherent problems of the KDD'99 dataset, making it more suitable for evaluating intrusion detection systems.

Key Features of NSL-KDD:
* Reduced Redundancy: Unlike the KDD'99 dataset, NSL-KDD does not contain redundant records, ensuring that the models do not become biased toward more frequent records.
* Balanced Distribution: It has a reasonable number of records, balancing the proportion between different types of attacks and normal connections.
* Realistic Scenario Representation: The dataset includes various types of intrusions simulated in a military network environment, offering a comprehensive overview of potential network threats.

This project uses the training data in the ARFF file type (converted to .csv), which does NOT contain the attack types and difficulty levels. This is available in the dataset within the .TXT files, but in the spirit of seeing how well the autoencoder can perform, I decided not to use those, at least to start with. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

To install prerequisities, simply do the following (ideally in a venv): 
* pip
  ```sh
  pip install -r requirements.txt 
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

  ```python
  python3.10 main.py 
  ```

Simple! This will train a model and output the resulting performance metrics in reports/figures/ , and to the command line. 


_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- To-do list -->
## To-do list

- [ ] .py files for EDA 
- [ ] More thorough outputs saved to disk 
- [ ] Hyperparameter grid search
- [ ] T-SNE analysis 
- [ ] PCA analysis 
- [ ] Full test data report 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Govindraj Singh Virdee - govindrajsinghv@gmail.com

Project Link: [https://github.com/govindvirdee/Military-Autoencoder](https://github.com/govindvirdee/Military-Autoencoder)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- [contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
 -->