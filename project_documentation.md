# Project Documentation
## QR-code intergation into accounting system

---

## 1. Project Overview

### 1.1 Project Title
QR-code intergation

### 1.2 Problem
The company currently uses outdated methods for tracking manufactured products:
- Employees manually mark products by writing their unique ID on paper stickers affixed to the product surface.
- Warehouse workers read the handwritten numbers and manually enter them into the accounting web application on tablets.
These manual processes create several critical issues:
- **Data accuracy errors**: Misspelled or misread identifiers lead to incorrect accounting records, inaccurate piecework wage calculations, unreliable production statistics, and unfair quality control assessments.
- **Inefficiency**: Manual writing and reading is time-consuming and slows down operations.
- **Security risks**: A large number of warehouse workers require full CRUD (create, read, update, delete) access rights in the accounting application, increasing the potential for data manipulation.

### 1.3 Project Description
This project involves integrating QR code technology into the enterprise's existing accounting system. Employees will use dedicated printing terminals to generate stickers containing QR codes with their unique EmployeeID. These stickers will be affixed to manufactured products for identification and tracking purposes. The QR codes will be scanned during warehouse receiving operations, enabling automated data capture for multiple business functions including piecework wage calculation, quality control, reporting, and planning. The QR code scanning system restricts not privileged application user permissions by eliminating manual edit capabilities, allowing only create and delete operations. This security measure prevents intentional manipulation of EmployeeID data.

### 1.4 Project Objectives
- Objective 1: Provide employees with RFID cards containing their encoded EmployeeID
- Objective 2: Design printing terminals with a user-friendly interface for quick QR code label generation
- Objective 3: Integrate QR code scanning functionality into the existing accounting system
- Objective 4: Ensure data security and implement validation mechanisms
- Objective 5: Conduct employee training on the new system operation

### 1.5 Scope
**In Scope:**
- What features and functionalities are included

**Out of Scope:**
- What features and functionalities are not included

### 1.6 Target Users
The system will be used by three primary user groups:
- **Production Workers**: use printing terminals to generate QR code labels for products they manufacture
- **Warehouse Staff**: scan QR codes during product receiving and inventory operations
- **Accounting Personnel**: access and analyze collected data for wage calculations, reporting, and production planning

---

## 2. System Requirements

### 2.1 Hardware Requirements

#### Printing Terminal Hardware
- **Compute Module:** Raspberry 4 or 5 (RPI)
- **RAM:** from 2GB
- **Storage:** from 16GB SD card
- **Display:** from 7" touchscreen, 800x480 resolution
- **RFID-Scanner:** based on RC522 chip
- **Printer:** Brother QL-500, QL-550, QL-560, QL-570, QL-580N, QL-650TD, QL-700, QL-710W, QL-720NW, QL-800, QL-810W, QL-820NWB, QL-1050, and QL-1060N
- **Connectivity:** printer via USB, RFID scanner via GPIO or USB
- **Power Supply:** 5V 3A adapter (RPI 5), 5V 5A adapter (RPI 5)
- **Additional Components:** case for touchscreen and RPI, connection cables, jumpers, RTC-battery for RPI

#### QR-code scanning
- **Scaner** qr-code scanner (HID-device)
- **Connectivity** bluetooth
- **Receiver** device with bluethooth, browser (Chrome recommended), and connection to internet (for access to accounting web application)

#### Additional equipment and materials
- **RFID cards** Mifare Classic 1K
- **Labels** Brother DK-11221 23x23mm

#### Development Hardware
- RPI 5 8Gb 
- 10.1" Waveshare touch screen with case
- RC522 chip
- Brother QL-700
- Sycreader W7

### 2.2 Software Requirements

#### Operating System
- **Printing Terminals** Linux (Raspberry Pi OS or others linux based) 
- **QR-code scanning** Windows, MacOS, Linux (web application works in browser)

#### Programming Languages
- Python 3.11, JavaScript, PL/SQL

#### Libraries, Frameworks and Databases
- GUI Framework: Tkinter/PyQt
- QR Code Libraries: see requirenments.txt
- Printer Libraries: see requirenments.txt
- SQLite3 (terminal), Oracle 21XE (web app)

#### Development Tools
- IDE: VS Codium, Pygubu/QtDesigner, Oracle APEX
- Version Control: Git
- Testing Tools: pytest, unittest, manual testing

### 2.3 Network Requirements
- Terminal works without internet connection and uses own database
- Internet connection for accounting web application is required

---

## 3. System Architecture

### 3.1 Architecture Diagram
[Insert diagram showing system components and their relationships]

```
┌─────────────────────────────────────┐
│         User Interface              │
│  (Touchscreen / Button Controls)    │
└────────────┬────────────────────────┘
             │
┌────────────▼────────────────────────┐
│      Application Logic Layer        │
│  - QR Scanner Module                │
│  - Data Processing Module           │
│  - Print Management Module          │
│  - Database/Storage Handler         │
└────────────┬────────────────────────┘
             │
┌────────────▼────────────────────────┐
│       Hardware Interface Layer      │
│  - Camera Driver                    │
│  - Printer Driver                   │
│  - Display Driver                   │
└─────────────────────────────────────┘
```

### 3.2 Component Description

#### 3.2.1 User Interface Module
- Purpose and functionality
- User interaction flow

#### 3.2.2 QR Code Scanner Module
- QR code detection algorithm
- Decoding process
- Error handling

#### 3.2.3 Data Processing Module
- Data validation
- Business logic
- Data transformation

#### 3.2.4 Print Management Module
- Print queue management
- Formatting and layout
- Printer communication

#### 3.2.5 Storage/Database Module
- Data structure
- Storage mechanism (local file, database, cloud)
- Data retrieval methods

---

## 4. Functional Requirements

### 4.1 QR Code Scanning
- **FR-1:** System shall detect QR codes within 2 seconds of presentation
- **FR-2:** System shall decode standard QR code formats (URL, text, vCard, etc.)
- **FR-3:** System shall provide visual/audio feedback upon successful scan
- **FR-4:** System shall handle multiple QR code formats
- **FR-5:** System shall validate scanned data before processing

### 4.2 Printing Functionality
- **FR-6:** System shall print scanned data in specified format
- **FR-7:** System shall support custom print templates
- **FR-8:** System shall handle print queue for multiple requests
- **FR-9:** System shall provide print preview (optional)
- **FR-10:** System shall report printer errors to user

### 4.3 User Interface
- **FR-11:** System shall provide clear instructions for scanning
- **FR-12:** System shall display scanned information before printing
- **FR-13:** System shall allow user confirmation before printing
- **FR-14:** System shall provide feedback on system status
- **FR-15:** System shall support multiple languages (optional)

### 4.4 Data Management
- **FR-16:** System shall log all scanning activities
- **FR-17:** System shall store scanned data with timestamp
- **FR-18:** System shall allow data export for reporting
- **FR-19:** System shall implement data retention policies

---

## 5. Non-Functional Requirements

### 5.1 Performance
- **NFR-1:** QR code detection latency: < 2 seconds
- **NFR-2:** Print job completion: < 10 seconds
- **NFR-3:** System boot time: < 30 seconds
- **NFR-4:** Continuous operation time: 8+ hours

### 5.2 Reliability
- **NFR-5:** System uptime: 99% during operating hours
- **NFR-6:** Error recovery: automatic restart on critical failures
- **NFR-7:** Data loss prevention: automatic backups

### 5.3 Usability
- **NFR-8:** Intuitive interface requiring minimal training
- **NFR-9:** Clear error messages and recovery instructions
- **NFR-10:** Accessibility features for users with disabilities

### 5.4 Security
- **NFR-11:** Data encryption for sensitive information
- **NFR-12:** Secure communication protocols
- **NFR-13:** Access control and authentication (if applicable)
- **NFR-14:** Regular security updates

### 5.5 Maintainability
- **NFR-15:** Modular code structure for easy updates
- **NFR-16:** Comprehensive logging for troubleshooting
- **NFR-17:** Remote monitoring capabilities (optional)

---

## 6. Design Specifications

### 6.1 User Interface Design

#### 6.1.1 Screen Layouts
[Include mockups or wireframes of each screen]

**Main Screen:**
- Layout description
- Button placements
- Display areas

**Scanning Screen:**
- Camera viewfinder
- Scan status indicators
- Cancel/retry options

**Results Screen:**
- Scanned data display
- Print/cancel buttons
- Edit options (if applicable)

**Settings Screen:**
- Configuration options
- System information

#### 6.1.2 User Flow Diagram
[Insert flowchart showing user journey through the system]

### 6.2 Database Schema (if applicable)

```sql
-- Example schema for scan logs
CREATE TABLE scan_logs (
    id INTEGER PRIMARY KEY,
    scan_timestamp DATETIME,
    qr_data TEXT,
    qr_type VARCHAR(50),
    print_status BOOLEAN,
    user_id VARCHAR(50)
);

-- Add your tables here
```

### 6.3 QR Code Format Specifications
- Supported QR code versions
- Data capacity limits
- Error correction levels
- Encoding formats (Numeric, Alphanumeric, Byte, Kanji)

### 6.4 Print Template Specifications
- Paper size and orientation
- Margins and spacing
- Font sizes and styles
- Logo/header placement
- Data field layout

---

## 7. Implementation Details

### 7.1 Development Phases

#### Phase 1: Hardware Setup (Week 1-2)
- Assemble terminal hardware
- Install operating system
- Configure peripherals
- Test basic functionality

#### Phase 2: Core Functionality (Week 3-5)
- Implement QR code scanning
- Develop data processing logic
- Integrate printer functionality
- Create basic UI

#### Phase 3: Advanced Features (Week 6-7)
- Add data validation
- Implement logging system
- Create custom print templates
- Add error handling

#### Phase 4: Testing & Refinement (Week 8-9)
- Unit testing
- Integration testing
- User acceptance testing
- Bug fixes and optimization

#### Phase 5: Documentation & Deployment (Week 10)
- Complete documentation
- User manual creation
- Deployment and installation

### 7.2 Code Structure

```
project_root/
├── src/
│   ├── main.py                 # Main application entry point
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── main_window.py     # Main UI window
│   │   └── widgets.py         # Custom UI widgets
│   ├── scanner/
│   │   ├── __init__.py
│   │   ├── qr_scanner.py      # QR scanning logic
│   │   └── decoder.py         # QR decode functions
│   ├── printer/
│   │   ├── __init__.py
│   │   ├── print_manager.py   # Print queue and management
│   │   └── templates.py       # Print templates
│   ├── data/
│   │   ├── __init__.py
│   │   ├── database.py        # Database operations
│   │   └── validator.py       # Data validation
│   └── utils/
│       ├── __init__.py
│       ├── logger.py          # Logging utilities
│       └── config.py          # Configuration management
├── tests/
│   ├── test_scanner.py
│   ├── test_printer.py
│   └── test_integration.py
├── docs/
│   ├── user_manual.md
│   └── api_documentation.md
├── config/
│   └── settings.json
├── resources/
│   ├── images/
│   └── templates/
├── requirements.txt
└── README.md
```

### 7.3 Key Algorithms

#### QR Code Detection Algorithm
```python
# Pseudocode for QR scanning
def scan_qr_code():
    1. Initialize camera
    2. Capture frame
    3. Preprocess image (grayscale, contrast adjustment)
    4. Detect QR code patterns
    5. If detected:
        a. Decode QR data
        b. Validate format
        c. Return decoded data
    6. Else:
        Retry or timeout
```

#### Print Job Processing
```python
# Pseudocode for printing
def process_print_job(data):
    1. Validate data format
    2. Load appropriate template
    3. Format data according to template
    4. Add to print queue
    5. Send to printer
    6. Monitor print status
    7. Log completion/errors
```

---

## 8. Testing Plan

### 8.1 Unit Testing
- **Scanner Module Tests**
  - Test QR code detection accuracy
  - Test various QR formats
  - Test error handling for invalid codes
  
- **Printer Module Tests**
  - Test print formatting
  - Test queue management
  - Test error recovery

- **Data Validation Tests**
  - Test input validation
  - Test data sanitization
  - Test edge cases

### 8.2 Integration Testing
- Camera-to-scanner integration
- Scanner-to-printer workflow
- Database read/write operations
- UI-to-backend communication

### 8.3 System Testing
- End-to-end user workflows
- Performance under load
- Stress testing (continuous operation)
- Recovery from failures

### 8.4 User Acceptance Testing
- Real-world usage scenarios
- User feedback collection
- Usability assessment
- Accessibility verification

### 8.5 Test Cases Example

| Test ID | Description | Input | Expected Output | Status |
|---------|-------------|-------|-----------------|--------|
| TC-001 | Scan valid URL QR code | QR with URL | URL displayed, ready to print | |
| TC-002 | Scan invalid QR code | Corrupted QR | Error message displayed | |
| TC-003 | Print scanned data | Valid scan data | Printed receipt | |
| TC-004 | Handle printer error | Print with no paper | Error message, retry option | |

---

## 9. Deployment

### 9.1 Installation Instructions

#### Prerequisites
- List all required hardware components
- List all software dependencies

#### Step-by-Step Installation
1. Hardware assembly
2. Operating system installation
3. Software dependencies installation
4. Application installation
5. Configuration setup
6. Initial testing

### 9.2 Configuration

#### Configuration File (config/settings.json)
```json
{
    "camera": {
        "device_id": 0,
        "resolution": [640, 480],
        "fps": 30
    },
    "printer": {
        "device_name": "/dev/usb/lp0",
        "paper_width": 80,
        "encoding": "UTF-8"
    },
    "qr_scanner": {
        "timeout": 30,
        "retry_attempts": 3
    },
    "database": {
        "path": "/var/data/scans.db",
        "backup_enabled": true
    }
}
```

### 9.3 Startup Procedure
1. Power on the terminal
2. System initialization sequence
3. Hardware checks
4. Application launch
5. Ready state

---

## 10. User Manual

### 10.1 Getting Started
- Power on instructions
- Initial setup (if required)
- Main screen overview

### 10.2 How to Scan QR Codes
1. Place QR code in front of camera
2. Wait for detection (green indicator)
3. Review scanned information
4. Confirm or retry

### 10.3 How to Print
1. After successful scan, review data
2. Press "Print" button
3. Wait for print completion
4. Retrieve printed document

### 10.4 Troubleshooting

| Problem | Possible Cause | Solution |
|---------|---------------|----------|
| QR code not detected | Poor lighting | Improve lighting or adjust angle |
| Blurry camera image | Dirty lens | Clean camera lens |
| Print not working | Printer offline | Check printer connection and paper |
| System frozen | Software crash | Restart terminal |

### 10.5 Maintenance
- Daily: Check paper supply, clean camera lens
- Weekly: Review error logs
- Monthly: Software updates, backup data

---

## 11. API Documentation (if applicable)

### 11.1 Internal APIs

#### Scanner API
```python
class QRScanner:
    def __init__(self, camera_id: int)
    def start_scanning(self) -> None
    def stop_scanning(self) -> None
    def get_last_scan(self) -> str
    def on_scan_complete(callback: Callable) -> None
```

#### Printer API
```python
class PrintManager:
    def __init__(self, printer_device: str)
    def add_to_queue(self, data: dict) -> int
    def print_now(self, data: dict) -> bool
    def get_queue_status(self) -> list
    def cancel_job(self, job_id: int) -> bool
```

### 11.2 External APIs (if integrated)
- API endpoints
- Authentication methods
- Request/response formats
- Rate limits

---

## 12. Security Considerations

### 12.1 Data Security
- Encryption methods used
- Secure storage practices
- Data anonymization (if applicable)

### 12.2 Network Security
- Firewall configuration
- Secure communication protocols
- VPN requirements (if applicable)

### 12.3 Physical Security
- Terminal placement recommendations
- Access control measures
- Tamper-proofing

### 12.4 Privacy Compliance
- GDPR compliance (if applicable)
- Data retention policies
- User consent mechanisms

---

## 13. Maintenance and Support

### 13.1 Regular Maintenance Tasks
- Software updates schedule
- Hardware inspection checklist
- Data backup procedures
- Log file rotation

### 13.2 Monitoring
- System health indicators
- Performance metrics
- Error rate tracking
- Usage statistics

### 13.3 Backup and Recovery
- Backup frequency
- Backup storage location
- Recovery procedures
- Disaster recovery plan

### 13.4 Support Contacts
- Technical support contact
- Emergency procedures
- Escalation path

---

## 14. Known Issues and Limitations

### 14.1 Current Limitations
- [e.g., Maximum QR code size: 100 characters]
- [e.g., Print speed: 50mm/s]
- [e.g., No color printing support]

### 14.2 Known Bugs
- [List any known issues with workarounds]

### 14.3 Future Improvements
- [e.g., Add barcode scanning support]
- [e.g., Implement cloud backup]
- [e.g., Add multi-language support]
- [e.g., Enhance UI with animations]

---

## 15. Project Timeline

### 15.1 Gantt Chart
[Insert timeline visualization]

| Phase | Task | Duration | Start Date | End Date | Status |
|-------|------|----------|------------|----------|--------|
| 1 | Hardware Setup | 2 weeks | | | |
| 2 | Core Development | 3 weeks | | | |
| 3 | Advanced Features | 2 weeks | | | |
| 4 | Testing | 2 weeks | | | |
| 5 | Documentation | 1 week | | | |

### 15.2 Milestones
- M1: Hardware assembly complete
- M2: QR scanning working
- M3: Printing functionality implemented
- M4: Testing complete
- M5: Project delivery

---

## 16. Budget and Resources

### 16.1 Hardware Costs
| Item | Quantity | Unit Price | Total |
|------|----------|------------|-------|
| Raspberry Pi 4 | 1 | $XX | $XX |
| Camera Module | 1 | $XX | $XX |
| Thermal Printer | 1 | $XX | $XX |
| Touchscreen | 1 | $XX | $XX |
| Case/Enclosure | 1 | $XX | $XX |
| Cables & Accessories | Various | $XX | $XX |
| **Total** | | | **$XXX** |

### 16.2 Software Costs
- Open-source libraries: Free
- Development tools: Free
- Optional cloud services: $XX/month

### 16.3 Time Resources
- Total development hours: XXX hours
- Team members: X people

---

## 17. References

### 17.1 Technical Documentation
- [QR Code specification: ISO/IEC 18004]
- [Library documentation links]
- [Hardware datasheets]

### 17.2 Learning Resources
- [Tutorials used]
- [Relevant courses]
- [Documentation sites]

### 17.3 Standards and Regulations
- [Relevant industry standards]
- [Safety certifications]
- [Compliance requirements]

---

## 18. Appendices

### Appendix A: Glossary
- **QR Code**: Quick Response code, 2D barcode format
- **Terminal**: Stand-alone device for scanning and printing
- **Throughput**: Number of scans/prints per minute
- [Add more terms as needed]

### Appendix B: Code Samples
[Include key code snippets or full modules]

### Appendix C: Circuit Diagrams
[Include hardware wiring diagrams if applicable]

### Appendix D: Additional Resources
- Links to repositories
- Additional documentation
- Community forums

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Your Name] | Initial draft |
| 1.1 | [Date] | [Your Name] | Added testing section |
| | | | |

**Last Updated:** [Date]  
**Document Owner:** [Your Name]  
**Review Date:** [Date]
