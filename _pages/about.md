---
permalink: /
author_profile: true
stylesheets:
  - /assets/css/home.css
redirect_from: 
  - /about/
  - /about.html
---
<h1 class="main-heading">Hi there <img src="images/Hi.gif" width="40px"> I'm Juyuan Wang!</h1>

I am an M.Sc. student at <a href="https://www.scut.edu.cn/">South China University of Technology (SCUT)</a>. My research interests focus on **Large Language Models (LLMs)**, **Retrieval-Augmented Generation (RAG)**, **Agents**, and **Information Retrieval**.

I am currently a research intern at **Tencent WXG (Search Application Department)**. Previously I worked at **Tencent WeChat AI (Pattern Recognition Center)**, **Weavin.ai**, and **China Southern Power Grid**.

Feel free to reach out via [Google Scholar](https://scholar.google.com/citations?user=21p1dyUAAAAJ&hl=zh-CN) if you are interested in collaboration or potential opportunities.

News
---------------
<div class="news-box">
  <ul class="news-list">
<li><span class="news-date"><em>2026.08</em></span> <strong>PonsRAG</strong> is available on <a href="https://arxiv.org/abs/2608.25486">arXiv</a>.</li>
<li><span class="news-date"><em>2026.01</em></span> Presented <strong>ComoRAG</strong> as a Poster at <strong>AAAI 2026</strong>. <a href="#moments">Photos →</a></li>

<li><span class="news-date"><em>2026.04</em></span> Our paper <strong>HeadRank</strong> is released on <a href="https://arxiv.org/abs/2604.17237">arXiv</a>.</li>

<li><span class="news-date"><em>2026.07</em></span> Represented the <strong>WeChat team</strong> at <strong>SIGIR 2026</strong> in Melbourne, presenting <strong>WeSEAL</strong> in an Oral session. <a href="#moments">Photos →</a></li>

<li><span class="news-date"><em>2025.12</em></span> 🎉 Our paper <strong>CoMoRAG</strong> (cognitive-inspired memory-organized RAG for stateful long narrative reasoning) is accepted by <strong>AAAI 2026</strong>.</li>

<li><span class="news-date"><em>2025.12</em></span> 🚀 I joined <strong>Tencent WXG (Search Application Department)</strong> as an LLM Algorithm Intern.</li>

<li><span class="news-date"><em>2025.09</em></span> 🎉 Our paper <strong>MVISU-Bench</strong> and <strong>HEAR</strong> are accepted by <strong>ACM MM 2025</strong>.</li>

<li><span class="news-date"><em>2025.09</em></span> 🚀 I joined <strong>Weavin.ai</strong> as a RAG Application Intern.</li>

<li><span class="news-date"><em>2025.02</em></span> 🚀 I joined <strong>Tencent WeChat AI (Pattern Recognition Center)</strong> through industry-university cooperation.</li>

<li><span class="news-date"><em>2024.09</em></span> 🚀 I joined <strong>China Southern Power Grid (CSG Smart)</strong> as an Algorithm Intern.</li>

  </ul>
</div>

Experience
--------------

<div class="experience-container">

  <div class="experience-card">
      <img src="images/logos/tencent.png" alt="Tencent logo" class="experience-logo">
      <div class="experience-info">
          <strong>Tencent — WXG, Search Application Department</strong><br>
          <em>2025.12 - Present</em><br>
          LLM Algorithm Intern<br>
          <span style="color:#888;">Working on LLM-based search, retrieval, and reasoning.</span>
      </div>
  </div>

  <div class="experience-card">
      <img src="images/logos/weavin.png" alt="Weavin logo" class="experience-logo">
      <div class="experience-info">
          <strong>Weavin.ai (智核未来)</strong><br>
          <em>2025.09 - 2025.11</em><br>
          RAG Application Development Intern<br>
          <span style="color:#888;">Building production-grade Retrieval-Augmented Generation systems for an AI startup.</span>
      </div>
  </div>

  <div class="experience-card">
      <img src="images/logos/wechat.png" alt="WeChat AI logo" class="experience-logo">
      <div class="experience-info">
          <strong>Tencent — WXG, Pattern Recognition Center (WeChat AI)</strong><br>
          <em>2025.02 - 2025.08</em><br>
          Industry-University Cooperation Researcher<br>
          <span style="color:#888;">Research on multimodal agents, document understanding, and information extraction.</span>
      </div>
  </div>

  <div class="experience-card">
      <img src="images/logos/csg.png" alt="CSG logo" class="experience-logo">
      <div class="experience-info">
          <strong>China Southern Power Grid — CSG Smart Technology</strong><br>
          <em>2024.09 - 2024.12</em><br>
          Algorithm Intern<br>
          <span style="color:#888;">Computer vision and transfer learning for power-grid asset recognition.</span>
      </div>
  </div>

  <div class="experience-card">
      <img src="images/logos/scut.png" alt="SCUT logo" class="experience-logo">
      <div class="experience-info">
          <strong>South China University of Technology</strong><br>
          <em>2024.09 - Present</em><br>
          M.Sc. Candidate<br>
          <span style="color:#888;">National Scholarship recipient. Multiple top-tier programming-contest awards (ICPC, CCPC, CCCC).</span>
      </div>
  </div>
</div>


Publications
--------------
<div class="pub-button-container"><button class="pub-button active" onclick="filterPublications(event, 'all')">Selected Publications</button><button class="pub-button" onclick="filterPublications(event, 'list')">Full Publications List</button></div>
<p class="publication-source">Eight papers indexed in <a href="https://scholar.google.com/citations?user=21p1dyUAAAAJ&amp;hl=zh-CN">Google Scholar</a>, plus one preserved additional record. Author order and publication details checked on October 4, 2026. Presentation and submission statuses are author-provided.</p>
<div id="core-publications" class="publication-view" data-publication-view="core">
<article class="publication-card updated-publication"><img class="publication-figure" src="/images/weseal.png" alt="WeSEAL: Well-calibrated Search for Eliminating Attention-sink Leakage method overview" loading="lazy"><div><h3>WeSEAL: Well-calibrated Search for Eliminating Attention-sink Leakage</h3><p class="publication-authors"><strong>Juyuan Wang</strong>, Chenxing Wang, Aolin Li, Huiyun Hu, Yuchen Fang, Haijun Wu, Jin Xu, Dongliang Liao</p><p>Calibration is internalized into model parameters for single-pass reranking in WeChat search. Presented on the SIGIR 2026 main stage in Melbourne on behalf of the WeChat team.</p><p><span class="pub-list-badge">SIGIR 2026 · Oral</span> <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;oe=ASCII&amp;user=21p1dyUAAAAJ&amp;pagesize=100&amp;citation_for_view=21p1dyUAAAAJ:M3ejUd6NZC8C">[Scholar / Paper]</a></p></div></article>
<article class="publication-card updated-publication"><img class="publication-figure" src="/images/comorag.png" alt="ComoRAG: A Cognitive-Inspired Memory-Organized RAG for Stateful Long Narrative Reasoning method overview" loading="lazy"><div><h3>ComoRAG: A Cognitive-Inspired Memory-Organized RAG for Stateful Long Narrative Reasoning</h3><p class="publication-authors"><strong>Juyuan Wang</strong>, Rongchen Zhao, Wei Wei, Yufeng Wang, Mo Yu, Jie Zhou, Jin Xu, Liyan Xu</p><p>A cognitive-inspired memory workspace for stateful long-narrative reasoning, with iterative probes, memory fusion, and hierarchical knowledge sources.</p><p><span class="pub-list-badge">AAAI 2026 · Poster</span> <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;oe=ASCII&amp;user=21p1dyUAAAAJ&amp;pagesize=100&amp;citation_for_view=21p1dyUAAAAJ:KlAtU1dfN6UC">[Scholar / Paper]</a> <a href="https://arxiv.org/abs/2508.10419">[arXiv]</a> <a href="https://github.com/EternityJune25/ComoRAG">[Code]</a></p></div></article>
<article class="publication-card updated-publication"><img class="publication-figure" src="/images/headrank.png" alt="HeadRank: Decoding-Free Passage Reranking via Preference-Aligned Attention Heads method overview" loading="lazy"><div><h3>HeadRank: Decoding-Free Passage Reranking via Preference-Aligned Attention Heads</h3><p class="publication-authors"><strong>Juyuan Wang</strong>, Chenxing Wang, Yuchen Fang, Huiyun Hu, Junwu Du, Aolin Li, Shunlin Rong, Haijun Wu, Jin Xu, Ligang Liu, Dongliang Liao</p><p>Decoding-free reranking through preference-aligned attention heads, entropy-regularized selection, and depth truncation.</p><p><span class="pub-list-badge">arXiv 2026 · ICLR 2027 submission</span> <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;oe=ASCII&amp;user=21p1dyUAAAAJ&amp;pagesize=100&amp;citation_for_view=21p1dyUAAAAJ:Zph67rFs4hoC">[Scholar / Paper]</a> <a href="https://arxiv.org/abs/2604.17237">[arXiv]</a></p></div></article>
<article class="publication-card updated-publication"><img class="publication-figure" src="/images/mvisu.png" alt="MVISU-Bench: Benchmarking Mobile Agents for Real-World Tasks by Multi-App, Vague, Interactive, Single-App and Unethical Instructions method overview" loading="lazy"><div><h3>MVISU-Bench: Benchmarking Mobile Agents for Real-World Tasks by Multi-App, Vague, Interactive, Single-App and Unethical Instructions</h3><p class="publication-authors">Zeyu Huang, <strong>Juyuan Wang</strong>, Longfeng Chen, Boyi Xiao, Leng Cai, Yawen Zeng, Jin Xu</p><p>A bilingual benchmark covering 404 real-world mobile-agent tasks across 137 apps and five instruction categories.</p><p><span class="pub-list-badge">ACM MM 2025 · Oral</span> <a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;oe=ASCII&amp;user=21p1dyUAAAAJ&amp;pagesize=100&amp;citation_for_view=21p1dyUAAAAJ:qxL8FJ1GzNcC">[Scholar / Paper]</a> <a href="https://arxiv.org/abs/2508.09057">[arXiv]</a> <a href="https://github.com/EternityJune25/MVISU-Bench">[Code]</a></p></div></article>
</div>
<div id="full-publications" class="publication-view" data-publication-view="list" hidden><ol class="full-publication-list">
<li><span class="pub-list-badge">SIGIR 2026 · Oral</span><span class="pub-list-title">WeSEAL: Well-calibrated Search for Eliminating Attention-sink Leakage</span><br><span class="pub-list-authors"><strong>Juyuan Wang</strong>, Chenxing Wang, Aolin Li, Huiyun Hu, Yuchen Fang, Haijun Wu, Jin Xu, Dongliang Liao</span><br><span class="publication-citation">Proceedings of the 49th International ACM SIGIR Conference on Research and Development in Information Retrieval, pp. 4976-4980.</span><br><span class="pub-list-links"><a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;oe=ASCII&amp;user=21p1dyUAAAAJ&amp;pagesize=100&amp;citation_for_view=21p1dyUAAAAJ:M3ejUd6NZC8C">[Scholar / Paper]</a></span></li>
<li><span class="pub-list-badge">SIGIR 2026 · Poster</span><span class="pub-list-title">When &amp; How to Write for Personalized Demand-aware Query Rewriting in Video Search</span><br><span class="pub-list-authors">Cheng Cheng, Chenxing Wang, Aolin Li, Haijun Wu, Huiyun Hu, <strong>Juyuan Wang</strong>, Dongliang Liao</span><br><span class="publication-citation">Proceedings of the 49th International ACM SIGIR Conference on Research and Development in Information Retrieval, pp. 4528-4533.</span><br><span class="pub-list-links"><a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;oe=ASCII&amp;user=21p1dyUAAAAJ&amp;pagesize=100&amp;citation_for_view=21p1dyUAAAAJ:ULOm3_A8WrAC">[Scholar / Paper]</a></span></li>
<li><span class="pub-list-badge">AAAI 2026 · Poster</span><span class="pub-list-title">ComoRAG: A Cognitive-Inspired Memory-Organized RAG for Stateful Long Narrative Reasoning</span><br><span class="pub-list-authors"><strong>Juyuan Wang</strong>, Rongchen Zhao, Wei Wei, Yufeng Wang, Mo Yu, Jie Zhou, Jin Xu, Liyan Xu</span><br><span class="publication-citation">Proceedings of the AAAI Conference on Artificial Intelligence, pp. 33557-33565.</span><br><span class="pub-list-links"><a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;oe=ASCII&amp;user=21p1dyUAAAAJ&amp;pagesize=100&amp;citation_for_view=21p1dyUAAAAJ:KlAtU1dfN6UC">[Scholar / Paper]</a> <a href="https://arxiv.org/abs/2508.10419">[arXiv]</a> <a href="https://github.com/EternityJune25/ComoRAG">[Code]</a></span></li>
<li><span class="pub-list-badge">arXiv 2026 · ICLR 2027 submission</span><span class="pub-list-title">HeadRank: Decoding-Free Passage Reranking via Preference-Aligned Attention Heads</span><br><span class="pub-list-authors"><strong>Juyuan Wang</strong>, Chenxing Wang, Yuchen Fang, Huiyun Hu, Junwu Du, Aolin Li, Shunlin Rong, Haijun Wu, Jin Xu, Ligang Liu, Dongliang Liao</span><br><span class="publication-citation">arXiv preprint arXiv:2604.17237.</span><br><span class="pub-list-links"><a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;oe=ASCII&amp;user=21p1dyUAAAAJ&amp;pagesize=100&amp;citation_for_view=21p1dyUAAAAJ:Zph67rFs4hoC">[Scholar / Paper]</a> <a href="https://arxiv.org/abs/2604.17237">[arXiv]</a></span></li>
<li><span class="pub-list-badge">arXiv 2026 · EMNLP 2026 Poster</span><span class="pub-list-title">PonsRAG: A Pons-Inspired RAG Bridging Cognitive Islands for Coordinated Long Narrative Reasoning</span><br><span class="pub-list-authors">Rongchen Zhao, Yu Chen, <strong>Juyuan Wang</strong>, Zhouting Mo, Jianxing Yu, Wenqing Chen, Jingping Liu</span><br><span class="publication-citation">arXiv preprint arXiv:2608.25486.</span><br><span class="pub-list-links"><a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;oe=ASCII&amp;user=21p1dyUAAAAJ&amp;pagesize=100&amp;citation_for_view=21p1dyUAAAAJ:YOwf2qJgpHMC">[Scholar / Paper]</a> <a href="https://arxiv.org/abs/2608.25486">[arXiv]</a></span></li>
<li><span class="pub-list-badge">ACM MM 2025 · Oral</span><span class="pub-list-title">MVISU-Bench: Benchmarking Mobile Agents for Real-World Tasks by Multi-App, Vague, Interactive, Single-App and Unethical Instructions</span><br><span class="pub-list-authors">Zeyu Huang, <strong>Juyuan Wang</strong>, Longfeng Chen, Boyi Xiao, Leng Cai, Yawen Zeng, Jin Xu</span><br><span class="publication-citation">Proceedings of the 33rd ACM International Conference on Multimedia, pp. 8797-8805.</span><br><span class="pub-list-links"><a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;oe=ASCII&amp;user=21p1dyUAAAAJ&amp;pagesize=100&amp;citation_for_view=21p1dyUAAAAJ:qxL8FJ1GzNcC">[Scholar / Paper]</a> <a href="https://arxiv.org/abs/2508.09057">[arXiv]</a> <a href="https://github.com/EternityJune25/MVISU-Bench">[Code]</a></span></li>
<li><span class="pub-list-badge">ACM MM 2025 · Oral</span><span class="pub-list-title">HEAR: A Holistic Extraction and Agentic Reasoning Framework for Document Understanding</span><br><span class="pub-list-authors">Longfeng Chen, Zheng Xiao, <strong>Juyuan Wang</strong>, Zeyu Huang, Yawen Zeng, Jin Xu</span><br><span class="publication-citation">Proceedings of the 33rd ACM International Conference on Multimedia, pp. 14376-14382.</span><br><span class="pub-list-links"><a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;oe=ASCII&amp;user=21p1dyUAAAAJ&amp;pagesize=100&amp;citation_for_view=21p1dyUAAAAJ:_kc_bZDykSQC">[Scholar / Paper]</a></span></li>
<li><span class="pub-list-badge">ISCTIS 2023</span><span class="pub-list-title">A Multi-task Learning and Transfer Learning-based Model for Crop Leaf Disease Identification</span><br><span class="pub-list-authors"><strong>Juyuan Wang</strong></span><br><span class="publication-citation">2023 3rd International Symposium on Computer Technology and Information Science (ISCTIS), pp. 348-355.</span><br><span class="pub-list-links"><a href="https://scholar.google.com/citations?view_op=view_citation&amp;hl=en&amp;oe=ASCII&amp;user=21p1dyUAAAAJ&amp;pagesize=100&amp;citation_for_view=21p1dyUAAAAJ:4TOpqqG69KYC">[Scholar / Paper]</a></span></li>
<li><span class="pub-list-badge">ICIHCS 2024 · Additional record</span><span class="pub-list-title">TL-DREN: Transfer Learning Based Detection and Recognition of Electricity Nameplates</span><br><span class="pub-list-authors">J. Li, B. Wen, K. Cai, Y. Li, M. Ma, X. Li, S. Tan, D. Wu, <strong>Juyuan Wang</strong>.</span><br><span class="publication-citation">Preserved from the previous homepage; not listed in the linked Scholar profile.</span></li></ol></div>
<script src="/assets/js/show_publications.js"></script>


Awards
--------
- *2023.05*, **14th ICPC (International Collegiate Programming Contest) — Bronze Medal**
- *2023.05*, **25th China Robot and Artificial Intelligence Competition — National Second Prize**
- *2023.05*, **16th China Collegiate Computer Design Competition — National Third Prize**
- *2022.12*, **4th National College Computer Ability Challenge — National Second Prize**
- *2022.08*, **8th China International "Internet+" Innovation & Entrepreneurship Competition — Provincial Second Prize**
- *2022.04*, **7th CCCC (China Collegiate Computer Programming Contest) Group Programming Ladder Tournament — National Second Prize**
- *2021.12*, **National Scholarship**
- *2021.10*, **3rd CCPC (China Collegiate Programming Contest) — Silver Medal**
- *2021.04*, **6th CCCC Group Programming Ladder Tournament — National Third Prize**


Services
--------
- Reviewer / volunteer for academic events in LLM, RAG, and IR communities.


Talks
--------
- **SIGIR 2026 · Melbourne, Australia** — Oral presentation of *WeSEAL: Well-calibrated Search for Eliminating Attention-sink Leakage*, representing the WeChat team alongside Chenxing Wang.
- **AAAI 2026 · Singapore** — Poster presentation and discussion of *ComoRAG: A Cognitive-Inspired Memory-Organized RAG for Stateful Long Narrative Reasoning*.


<h2 id="moments">Conference &amp; Life Moments</h2>
<p class="publication-source">Academic milestones and moments beyond the lab. Select a photo to view the full image.</p>
<section class="moment-group"><h3>SIGIR 2026 · Melbourne</h3><p>Representing the WeChat team on the SIGIR main stage, followed by moments from the Melbourne trip.</p><div class="moment-grid"><figure><a href="/images/moments/sigir-oral.jpg" target="_blank" rel="noopener"><img src="/images/moments/sigir-oral.jpg" alt="WeSEAL Oral presentation · SIGIR 2026 main stage" loading="lazy" decoding="async"></a><figcaption>WeSEAL Oral presentation · SIGIR 2026 main stage</figcaption></figure><figure><a href="/images/moments/melbourne-market.jpg" target="_blank" rel="noopener"><img src="/images/moments/melbourne-market.jpg" alt="Melbourne trip · evening market" loading="lazy" decoding="async"></a><figcaption>Melbourne trip · evening market</figcaption></figure><figure><a href="/images/moments/melbourne-wildlife.jpg" target="_blank" rel="noopener"><img src="/images/moments/melbourne-wildlife.jpg" alt="Melbourne trip · Australian wildlife" loading="lazy" decoding="async"></a><figcaption>Melbourne trip · Australian wildlife</figcaption></figure></div></section>
<section class="moment-group"><h3>AAAI 2026 · Poster</h3><p>Sharing ComoRAG and discussing stateful long-narrative reasoning with the research community.</p><div class="moment-grid single"><figure><a href="/images/moments/aaai-poster.jpg" target="_blank" rel="noopener"><img src="/images/moments/aaai-poster.jpg" alt="ComoRAG Poster presentation · AAAI 2026" loading="lazy" decoding="async"></a><figcaption>ComoRAG Poster presentation · AAAI 2026</figcaption></figure></div></section>
<section class="moment-group"><h3>Tencent Qingyun · Starlit Tech Gala</h3><p>Memories from the Tencent Qingyun closed-door evening event.</p><div class="moment-grid"><figure><a href="/images/moments/qingyun-night.jpg" target="_blank" rel="noopener"><img src="/images/moments/qingyun-night.jpg" alt="Starlit Tech Gala · city lights" loading="lazy" decoding="async"></a><figcaption>Starlit Tech Gala · city lights</figcaption></figure><figure><a href="/images/moments/qingyun-penguin.jpg" target="_blank" rel="noopener"><img src="/images/moments/qingyun-penguin.jpg" alt="Tencent penguin · evening venue" loading="lazy" decoding="async"></a><figcaption>Tencent penguin · evening venue</figcaption></figure><figure><a href="/images/moments/qingyun-gathering.jpg" target="_blank" rel="noopener"><img src="/images/moments/qingyun-gathering.jpg" alt="Tencent Qingyun · gathering and conversations" loading="lazy" decoding="async"></a><figcaption>Tencent Qingyun · gathering and conversations</figcaption></figure></div></section>
