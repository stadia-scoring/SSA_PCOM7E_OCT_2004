# Individual Reflection

This module was a deep dive into secure systems architecture, taking me from high-level risk management in Unit 3 to hands-on implementation in Unit 6. The progression highlighted the contrast between abstract system design and technical execution, challenging me to think critically about vulnerabilities while developing practical solutions. Through these experiences, I transitioned from collaborative group work to individual responsibility, honing my ability to navigate both theoretical and technical complexities.

## Reflections on Unit 3: Collaborative Design

The Unit 3 group project involved designing an Attack-Defence (AD) tree for an IoT-based System of Systems (SoS), a method inspired by Schneier's (1999) framework for breaking down complex attack vectors. My contributions focused on identifying vulnerabilities, such as insecure communication protocols and insufficient access controls, both commonly recognized challenges in IoT security (IBM Developer, 2020). These were mapped onto the AD tree alongside suggested mitigations.

Collaborating with peers highlighted the importance of diverse perspectives in tackling multi-faceted problems like IoT security (Venkatraman et al., 2021). However, agreeing on risk prioritization proved challenging. For instance, while some team members favored addressing device authentication, others prioritized data transmission vulnerabilities. This forced us to critically evaluate risk domains and their impacts on the overall system.

## Reflections on Unit 6: Individual Implementation

Building on the AD tree, my Unit 6 project explored a question tied to the “Connectivity” characteristic of SoS: **“Is encrypting individual parts of a data transfer more efficient and secure than encrypting the entire payload?”** This required transitioning from abstract design to a working prototype in Python, simulating data interactions between an IoT client and hub.

The implementation phase revealed practical challenges. For instance, encrypting sections of data improved granularity and allowed selective security but introduced latency due to the computational overhead—an issue echoed in MDPI's (2018) findings on IoT protocol performance. Addressing these trade-offs required optimizing encryption algorithms and employing lightweight techniques like selective compression.

Unlike the theoretical exercise of Unit 3, Unit 6 required deeper technical engagement. I utilized containerized environments for testing and deployment, a practice recommended for scalability in IoT development (Docker Inc., 2021). Iterative testing was essential, exposing issues that high-level risk models couldn’t predict, such as timing delays under load. This hands-on phase not only strengthened my programming skills but also emphasized the need to balance security and system performance.

## Emotional and Analytical Reflections

While I appreciated the collaboration in Unit 3, I found myself thriving in the independence of Unit 6. Individual work gave me the freedom to experiment with unconventional ideas, such as optimizing encryption processes, without the constraints of group consensus. This mirrors the broader industry trend where flexibility fosters innovation in smaller, focused teams.

Seeing tangible results from my prototype was immensely rewarding. When selective encryption successfully demonstrated better resource efficiency under specific conditions, it validated the effort invested in technical problem-solving. Conversely, recognizing the practical limitations of static AD tree models reinforced the need for dynamic risk assessment tools.

## Growth Plan and Actionable Steps

| **Skill**                   | **Current Proficiency** | **Development Goals**                        | **Action Plan**                                              |
|-----------------------------|-------------------------|----------------------------------------------|-------------------------------------------------------------|
| Vulnerability Management    | Proficient             | Deepen understanding of dynamic risk modeling | Explore advanced techniques like attack graphs and simulations |
| Programming and Optimization| Intermediate           | Enhance Python proficiency and resource optimization | Study encryption techniques tailored for IoT                 |
| Testing and Debugging       | Intermediate           | Expand automated testing capabilities         | Experiment with fuzzing tools and TDD methodologies          |
| Communication and Teamwork  | Proficient             | Balance collaborative and independent work styles | Seek projects that integrate teamwork with individual exploration |

## Conclusion

Reflecting on this module, I’ve gained a deeper appreciation for the bridge between high-level design and practical implementation. Moving from the collaborative AD tree exercise to an individual prototype demonstrated how theoretical models must evolve to address real-world challenges. The flexibility and focus of individual work allowed me to refine my critical thinking and technical skills, and the lessons learned will undoubtedly inform my approach to future secure system designs.

## References

- Docker Inc. (2021) Containerized Python Development – Part 1. Available at: [https://www.docker.com/blog/containerized-python-development-part-1/](https://www.docker.com/blog/containerized-python-development-part-1/) (Accessed: 30 November 2024).
- IBM Developer (2020) Top 10 IoT Security Challenges. Available at: [https://developer.ibm.com/articles/iot-lp101-connectivity-network-protocols/](https://developer.ibm.com/articles/iot-lp101-connectivity-network-protocols/) (Accessed: 29 November 2024).
- MDPI (2018) Security of IoT Application Layer Protocols: Challenges and Findings. *Future Internet*, 12(3), p.55. Available at: [https://www.mdpi.com/2411-9660/3/3/32](https://www.mdpi.com/2411-9660/3/3/32) (Accessed: 28 November 2024).
- Rios, E., Rego, A., Iturbe, E., Higuero, M. and Larrucea, X. (2020) ‘Continuous quantitative risk management in smart grids using attack defense trees’, *Sensors*, 20(16), 4404. Available at: [https://doi.org/10.3390/s20164404](https://doi.org/10.3390/s20164404) (Accessed: 30 November 2024).
- Schneier, B. (1999) Attack Trees. Available at: [https://www.schneier.com/academic/archives/1999/12/attack_trees.html](https://www.schneier.com/academic/archives/1999/12/attack_trees.html) (Accessed: 28 November 2024).
- ScienceDirect (2018) A Review of Smart Cities Based on the Internet of Things Concept. *Journal of Cleaner Production*. Available at: [https://www-sciencedirect-com.uniessexlib.idm.oclc.org/science/article/pii/S0959652618339775?via%3Dihub](https://www-sciencedirect-com.uniessexlib.idm.oclc.org/science/article/pii/S0959652618339775?via%3Dihub) (Accessed: 29 November 2024).
- Venkatraman, S., Overmars, A. and Thong, M. (2021) ‘Smart home automation—use cases of a secure and integrated voice-control system’, *Systems*, 9(4), p.77. Available at: [https://doi.org/10.3390/systems9040077](https://doi.org/10.3390/systems9040077) (Accessed: 30 November 2024).
