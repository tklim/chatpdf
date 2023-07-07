# chatpdf
Embed your own PDF files into chat query

1. Save your PDF file you wish to query into /data/docs (for example)
2. Create .env with your own OpenAI APIKEY
3. Edit chatpdf.py with the path of your PDF files, and update the query you want
4. Run chatpdf.py

Below is a sample output:
```# ./chatpdf.py
<class 'list'>
file_path= /data/docs/gartner/2023-gartner-top-strategic-technology-trends.pdf
<class 'list'>
done chucks
token_counts= [542, 543, 519, 488, 537, 537, 539, 537, 477, 511, 546, 535, 480, 540, 510, 534, 542, 520, 287]
[1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 1 0 0 2 2 0
 0 6 5]
  6 +-----------------------------------------------------------------------+
    |                                                                   *   |
    |                                                                   **  |
  5 |                                                                   **  |
    |                                                                   *   |
    |                                                                   *   |
    |                                                                  *    |
  4 |                                                                  *    |
    |                                                                  *    |
    |                                                                  *    |
  3 |                                                                  *    |
    |                                                                  *    |
    |                                                                  *    |
    |                                                                  *    |
  2 |                                                     *       **   *    |
    |                                                     *       **   *    |
    |                                                    * *     *  * *     |
  1 |        *                                           * * *   *  * *     |
    |        *                                           * * **  *  * *     |
    |         *                                          * * **  *  * *     |
    |         *                                         *   *  **    **     |
  0 +-----------------------------------------------------------------------+
   250         300         350         400         450         500         550
embeddings
out=  Gartner provides an annual list of key technology trends that both business leaders and technologists should leverage in the next 36 months, including Sustainable Technology, AI TRiSM, Wireless Value Realization, Industry Cloud Platforms, Digital Immune System, Platform Engineering, and Superapps. Four pillars of AI trust, risk and security management are Explainability/Model Monitoring, AI Application Security, Privacy, and ModelOps. Strategic Technology Trends 2023 include making AI models explainable or interpretable. Industry Cloud Platforms create value for organizations by incorporating cloud services into preintegrated but customizable (composable) industry-relevant solutions. Intelligent infrastructure strategies should be designed to select the right technologies and vendors for wireless systems of the future. Adaptive AI systems allow for model behavior change postdeployment by learning from past experience and adapting to changing real-world circumstances. AI engineering provides foundational components to enable adaptive AI systems.
```
