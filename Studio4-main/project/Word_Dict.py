# -*- coding: utf-8 -*-

def word_category():
    word_dict = {

        'อาหาร'     :['อาหาร','ทำอาหาร','เครื่องปรุง','วัตถุดิบ','ไข่','ของหวาน',   'ของกิน','โภชนาการ','แฮม','เจ','กินเจ','มังสวิรัติ','กุ้ง','หอย','วัว','หมู','หมึก','สาหร่าย','เป็ด','ปลา','ปู','เนื้อ','สลัด','ข้าวต้ม','ข้าวปั้น','ข้าวผัด','กะปิ','ปลาร้า','ขนมปัง','ซุป','น้ำพริก','ข้าวเหนียว','ลาบ','กะเพรา','ซาบะ','ส้มตำ','ไส้กรอก','ปูอัด','เบคอน','บะหมี่','ก๋วยเตี๋ยว','ลูกชิ้น','วุ้นเส้น','ขนมจีน'],
        'ทำอาหาร'   :['ปรุง','ทอด','แกง','ผัด','เจียว','ปิ้ง','เตา','ครัว','ครก','กระทะ','หม้อ','หุงข้าว'],
        'เครื่องปรุง'  :['เกลือ','เครื่องเทศ','ซอส','พริกไทย',],
        'วัตถุดิบ'     :['แป้ง','ส่วนผสม','เนย','กะทิ','ข้าวสาลี','ธัญพืช','เต้าเจี้ยว'],
        'ไข่'        :['ไข่ไก่','ไข่เยี่ยวม้า','ไข่เป็ด','ไข่นกกระทา','ไข่ต้ม','ไข่ดาว','ไข่เจียว','ไข่ข้าว','ไข่ลูกเขย','เปลือกไข่'],
        'ของหวาน'   :['ขนม','ครีม','เค้ก','ไอศกรีม','ช็อกโกแลต','น้ำผึ้ง','กล้วยบวดชี','บัวลอย'],

        'เครื่องดื่ม'   :['เครื่องดื่ม','นม','กาแฟ','ชา','ชาเย็น','น้ำอัดลม','นำ้ผลไม้','ชานมไข่มุก','ไวน์','สุรา','เหล้า','ค็อกเทล','เบียร์','โซดา','เครื่องดื่มชูกำลัง','เก๊กฮวย',],

        'ผลไม้'      :['ผลไม้','กล้วย','ส้ม',   'กีวี่','กระท้อน','แก้วมังกร','ขนุน','แคนตาลูป','เงาะ','เชอร์รี่','น้อยหน่า','ทุเรียน','พุทรา','มะพร้าว','มะม่วง','มะขาม','มะละกอ','มังคุด','ราสเบอร์รี่','ลำไย','ละมุด','ลิ้นจี่','ลองกอง','ส้มโอ','เสาวรส','สาลี่','สับปะรด','สตรอว์เบอร์รี','หม่อน','องุ่น','แอปเปิ้ล','แตงไทย','แตงโม'],
        'กล้วย'      :['กล้วยน้ำว้า','กล้วยไข่','กล้วยหอม','กล้วยเล็บมือนาง'],
        'ส้ม'        :['ส้มเขียวหวาน','ส้มเช้ง','ส้มสายน้ำผึ้ง','ส้มจีน','ส้มจี๊ด'],

        'ผัก'        :['ผัก','กะหล่ำ','กะหล่ำปลี','กระเทียม','ขิง','ข่า','ข้าวโพด','แครอท','คะน้า','ชะอม','ผักกาด','ผักกระเฉด','ผักชี','ผักบุ้ง','พริก','ตะไคร้','ตำลึง','แตงกวา','ถั่วงอก','ถั่วฝักยาว','บร็อคโคลี่','มะนาว','มะเขือเปราะ','มะเขือเทศ','มะระ','มันฝรั่ง','สะตอ','เห็ด'],

        'คอมพิวเตอร์' :['คอมพิวเตอร์','โน้ตบุ๊ค','เมาส์','ซีพียู','คีย์บอร์ด'],
        
        'มือถือ'      :['มือถือ','โทรศัพท์','แอปพลิเคชัน',],

        'โปรแกรม'   :['โปรแกรม','โปรแกรมคอมพิวเตอร์','เว็บ','ซอฟต์แวร์'],

        'กีฬา'       :['กีฬา','ฟุตบอล','บาสเกตบอล','มวย','แบดมินตัน','หมากกระดาน',   'กรีฑา','กอล์ฟ','คาราเต้','เทควันโด','ตะกร้อ','ยกน้ำหนัก','ยิมนาสติก','รักบี้','วอลเลย์บอล','สกี','สนุกเกอร์','เซปักตะกร้อ','เทนนิส','เปตอง','ปิงปอง','เบสบอล','แฮนด์บอล','ซอฟท์บอล','โอลิมปิก','พาราลิมปิก','ตัวสำรอง','นักกีฬา','สนามกีฬา','วิทยาศาสตร์การกีฬา','วิ่งมาราธอน'],
        'ฟุตบอล'     :['ลูกหนัง','สโมสร','แฟนบอล','นักฟุตบอล','นักเตะ','ค้าแข้ง','เตะบอล','ลูกบอล','บอล','ฟุตบอลโลก','พรีเมียร์ลีก','ดาวรุ่ง','ใบเหลือง','ใบแดง','ล้ำหน้า','ลูกโทษ','เขตโทษ','ผู้รักษาประตู','กองหน้า','กองกลาง','กองหลัง'],
        'แบดมินตัน'   :['ลูกขนไก่','ไม้แบด'],
        'บาสเกตบอล' :['บาส','ลูกบาส','แป้นบาส'],
        'มวย'       :['ชกมวย','มวยไทย','มวยสากล','สังเวียน','สนามมวย','แขวนนวม','นักมวย','เข็มขัดแชมป์','นวม','เมาหมัด','กระสอบทราย','น้ำมันมวย'],
        'หมากกระดาน':['หมากรุก','หมากฮอส','หมากล้อม','โอเทลโล่'],

        'ว่ายน้ำ'     :['ว่ายน้ำ','ชุดว่ายน้ำ','สระว่ายน้ำ'],
        
        'สัตว์'       :['สัตว์','สัตว์น้ำ','สัตว์เลื้อยคลาน','สัตว์เลี้ยง','นก','เสือ','ลิง',   'กบ','กระทิง','กระบือ','กระรอก','ควาย','คางคก','ค้างคาว','จิงโจ้','จิ้งจอก','ชะมด','ตะพาบ','นาก','ยีราฟ','สิงโต','ห่าน','หงส์','หนู','หมาจิ้งจอก','หมาป่า','หมี','หมีขาว','หมีขั้วโลก','หมูป่า','อีเห็น','อูฐ','เลียงผา','แกะ','แพะ','แรด','โค','เม่น','สวนสัตว์'],
        'สัตว์น้ำ'     :['กระเบน','ฉลาม','ปลาตะเพียน','ปักเป้า','พะยูน','ม้าน้ำ','วาฬ','โลมา'],
        'สัตว์เลื้อยคลาน':['งู',    'กิ้งก่า','จระเข้','จิ้งจก','จิ้งเหลน','ตุ๊กแก','ตะกวด','ตัวเงินตัวทอง'],
        'งู'         :['งูพิษ','งูเหลือม','งูเห่า','งูจงอาง','งูหลาม','งูเขียว','งูหางกระดิ่ง','งูแมวเซา'],
        'สัตว์เลี้ยง'   :['หมา','แมว',   'เลี้ยงสัตว์','แฮมสเตอร์','กระต่าย','ปลาทอง','ปลอกคอ'],
        'หมา'       :['สุนัข','อาหารหมา'],
        'แมว'       :['เหมียว','อาหารแมว'],
        'นก'        :['นกกระจอก','นกยูง','นกแก้ว','นกแสก','นกพิราบ','นกเงือก','นกหัวขวาน','นกกระเรียน','นกฮูก','นกกระจอกเทศ','เพนกวิน','นกอินทรี','เหยี่ยว','แร้ง'],
        'เสือ'       :['พยัคฆ์','เสือดาว','เสือโคร่ง'],
        'ลิง'        :['ลิงลม','วานร','กอริลลา','ชิมแปนซี','อุรังอุตัง','ลิงแสม'],

        'แมลง'      :['แมลง','มด',   'แมลง','จิ้งหรีด','ตะขาบ','กิ้งกือ','ตั๊กแตน','ผีเสื้อ','ผึ้ง','ยุง','หนอน','ด้วง','แตน','เต่าทอง','แมง','แมงมุม','แมลงปอ','แมลงวัน','แมลงสาบ','แมลงเม่า'],
        'มด'        :['มดแดง','มดดำ','รังมด'],

        'เทศกาล'    :['เทศกาล','คริสต์มาส','สงกรานต์','ตรุษจีน','เช็งเม้ง'],

        'อาวุธ'      :['อาวุธ','ระเบิด','ปืน',   'ดาบ','ขวาน','กระบอง','โล่','เกราะ','กระบี่','ตะบอง','ธนู','มีด','หอก'],
        'ระเบิด'     :['ระเบิดมือ','ลูกระเบิด','ตอร์ปิโด','ระเบิดเวลา','วางระเบิด','ไดนาไมต์'],
        'ปืน'        :['กระสุนปืน',   'ไรเฟิล','ปืนยาว','ปืนสั้น','ปืนพก','ปืนกล'],
        'กระสุนปืน'   :['กระสุน','ดินปืน'],

        'งานบ้าน'    :['งานบ้าน','ซักผ้า','ตากผ้า','รีดผ้า','เย็บผ้า','ล้างจาน'],
        'ซักผ้า'      :['ซัก','ซักรีด','ผงซักฟอก','น้ำยาซักผ้า','น้ำยาปรับผ้านุ่ม'],
        'รีดผ้า'      :['รีด','น้ำยารีดผ้า'],    

        'แต่งตัว'     :['แต่งตัว','กระโปรง','กางเกง','ชุด','รองเท้า','สูท','เสื้อ','เสื้อผ้า','หมวก','เข็มขัด','เครื่องแบบ','แฟชั่น'],

        'เพศ'       :['เพศ','เพศหญิง','เพศชาย','กะเทย'], 
        'เพศหญิง'    :['ผู้หญิง','หญิง','ตัวเมีย','สตรี'],
        'เพศชาย'    :['ผู้ชาย','ชาย','ตัวผู้',],

        'ฝัน'        :['ฝัน','ฝันดี','ฝันร้าย','ฝันกลางวัน','ความฝัน'],
        
        'ถ่ายรูป'     :['ถ่ายรูป','รูปถ่าย','ภาพนิ่ง','กล้อง','กล้องถ่ายรูป'],

        'ท่องเที่ยว'   :['ท่องเที่ยว','นักท่องเที่ยว','สถานที่ท่องเที่ยว','กระเป๋าเดินทาง','รีสอร์ท','ที่พัก','โรงแรม','โฮมสเตย์','ที่เที่ยว'],

        'ดวงชะตา'   :['ดวงชะตา','ดวง','ดูดวง','ชะตา','โชค','โชคชะตา','ฮวงจุ้ย','โหงวเฮ้ง','เซียมซี','โหราศาสตร์','โหราจารย์','ราศี'],

        'ภัย'        :['ภัย','อันตราย','อุบัติเหตุ','ไฟไหม้','ไฟฟ้าลัดวงจร','นำ้ท่วม','รถชน','ทุพภิกขภัย','วาตภัย','แผ่นดินไหว','พายุ','น้ำป่า'], 

        'อาชญากรรม' :['อาชญากรรม','โจร','ขโมย','ปล้น','ชิงทรัพย์','วิ่งราว','ลวนลาม','ข่มขืน','ทารุณกรรม','ฆาตกร','ฆาตกรรม','คนร้าย','ผู้ต้องหา'],

        'การเรียน'   :['โรงเรียน',   'เรียน','การเรียน','การศึกษา','มหาวิทยาลัย','เรียนต่อ','เรียนพิเศษ','ทุนการศึกษา','รายวิชา','ภาคเรียน','ความรู้','แนะแนว','พลศึกษา','เรียนรู้','ครุ','วิชาเอก','อาชีวศึกษา','หลักสูตร','วิชาการ','วิทยาเขต','ปีการศึกษา','ข้อสอบ','การบ้าน','ทำการบ้าน','ตำรา','ลูกเสือ','ครู','คะแนน','ติว','สอบ','นักเรียน','ศึกษาธิการ','อาจารย์','ลูกศิษย์','ชมรม','วิทยา','คณาจารย์','เล่าเรียน','วิชา','หน่วยกิต','มัธยมศึกษา','มัธยม','มัธยมต้น','มัธยมปลาย','สหศึกษา','ประถม','อนุบาล','เทอม','เปิดเทอม','ปิดเทอม','ค่าเทอม','ผลการเรียน'],
        'โรงเรียน'   :['โรงเรียนประจำ','คอนแวนต์','โรงเรียนสาธิต','โรงเรียนรัฐ','โรงเรียนเอกชน','โรงเรียนกวดวิชา'],
        'มหาวิทยาลัย' :['ปริญญา','ปริญญาตรี','ปริญญาโท','ปริญญาเอก','ปริญญาบัตร','ดุษฎีบัณฑิต','มหาบัณฑิต','อนุปริญญา','เกียรตินิยม','วิทยานิพนธ์','เนติบัณฑิต','วิทยาลัย','มหาลัย','นักศึกษา','บัณฑิต','นิสิต','จุฬา','ธรรมศาสตร์','เกษตรศาสตร์','ราชภัฏ','อุดมศึกษา'],
        
        'ของมีค่า'    :['ของมีค่า','ทอง','ทองคำ','ทองรูปพรรณ','สร้อยทอง','ทองคำขาว','เพชร','หยก','งาช้าง','อัญมณี','แหวน','ไข่มุก','พลอย','สมบัติ'],

        'เพื่อน'      :['เพื่อน','เพื่อนสนิท','มิตร'],

        'การ์ตูน'     :['การ์ตูน','หนังสือการ์ตูน','มังงะ','อนิเมะ','นักเขียนการ์ตูน','โดจิน'],

        'หนังสือ'     :['หนังสือ','วรรณกรรม','นวนิยาย','นิยาย','วรรณคดี','นิทาน','สิ่งพิมพ์','โรงพิมพ์','พิมพ์หนังสือ','นิตยสาร','สำนักพิมพ์','บรรณาธิการ','หนังสือพิมพ์','วารสาร','สารานุกรม','นักเขียน','นามปากกา','ห้องสมุด','หอสมุด','อ่านหนังสือ'],
        
        'บทความ'    :['บทความ','สารคดี','คอลัมน์','สัมภาษณ์'],
        
        'เรื่องแต่ง'   :['เรื่องแต่ง','เนื้อหา','ฉาก','เนื้อเรื่อง','ตัวละคร','พระเอก','นางเอก','ตัวเอก','ตัวประกอบ',],

        'สื่อมวลชน'   :['สื่อมวลชน','ข่าว','ข่าวสด','ข่าวสาร','สื่อ','พิธีกร','นักข่าว','ผู้สื่อข่าว','สื่อสารมวลชน','วิทยุโทรทัศน์','กระจายเสียง','วิทยุกระจายเสียง',],
        
        'โทรคมนาคม' :['โทรคมนาคม','การสื่อสาร','สารสนเทศ','ดาวเทียม','สัญญาณ','เคเบิล','คลื่นวิทยุ','คลื่น','ความถี่',],
        
        'บันเทิง'     :['บันเทิง','ภาพยนตร์','ละคร','ละครโทรทัศน์','ดารา','เวที','นางแบบ','นางงาม','ถ่ายแบบ','ดารา','นักแสดง'],
        
        'ดนตรี'      :['ดนตรี','เครื่องดนตรี','ดนตรีไทย','ดนตรีสากล','เพลง','ร้องเพลง','ทำนอง','ขับร้อง','บทเพลง','เนื้อร้อง','คำร้อง','เนื้อเพลง','คอนเสิร์ต','ประสานเสียง','ผู้อำนวยเพลง','ดุริยางค์','ลูกทุ่ง','หมอลำ','โน้ต','คอร์ด','แผ่นเสียง',],
        'เครื่องดนตรี' :['กลอง','เบส','กีตาร์','ขลุ่ย','เปียโน','ไวโอลิน','ระนาด','แตร','เครื่องสาย','ออร์แกน','ระนาดเอก',],
        
        'ศิลปะ'      :['ศิลปะ','ศิลป์','จิตรกรรม','วาดภาพ','ประติมากรรม','ภาพประกอบ','จิตรกร','วาด','ปูนปั้น','ลงรัก','วิจิตรศิลป์','ทัศนศิลป์','ลวดลาย','รูปทรง','สีสัน','สุนทรียศาสตร์','ลายเส้น',],
        'การแสดง'   :['การแสดง','โขน','ลิเก','โนรา','หนังตะลุง','เต้นรำ','รำ','ระบำ','เต้น','นาฏศิลป์','ละครเวที','งิ้ว','โชว์',],
        
        'วิทยาศาสตร์' :['วิทยาศาสตร์','วิทย์','ชีววิทยา','ฟิสิกส์','เคมี','ดาราศาสตร์','อะตอม',],

        'เจ็บป่วย'    :['เจ็บป่วย','โรคประจำตัว','โรคติดต่อ',   'ปวดหัว','ตัวร้อน','เป็นไข้','คลื่นไส้','อาเจียน','แขนหัก','ขาหัก','กระดูกหัก','เสมหะ','ซึมเศร้า','ท้องเสีย','ท้องผูก','อัมพาต','ปวด','ชัก','แผล','ตุ่ม','พยาธิ','เจ็บปวด','ตาบอด','เคล็ด','หูหนวก','ตาเหล่','หวัด','ปวดร้าว','ตีบ','ปวดแสบปวดร้อน','เจ็บไข้','ไอ','เป็นลม','เจ็บท้อง','เจ็บ','เนื้อร้าย','เนื้องอก','ประสาทหลอน','มะเร็ง','โรคประสาท','วัณโรค','ฝี','โรคจิต','เชื้อโรค','โรคจิตเภท','กาฬโรค','ดื้อยา','ตับแข็ง','เหา','งูสวัด','โรคสมอง','โรค','ติดเชื้อ','อักเสบ','ป่วย','พิการ','บกพร่อง','เรื้อรัง','แพลง','วาย','โปลิโอ','เมื่อย','กรน'],
        'โรคประจำตัว':['เบาหวาน','ความดัน','ภูมิแพ้','ริดสีดวง','เกาต์','ปอดบวม','โลหิตจาง','หอบหืด'],
        'โรคติดต่อ'   :['โควิด','ไข้เลือดออก','มาลาเรีย','ซิฟิลิส','อหิวาตกโรค','กามโรค','เอดส์','โรคระบาด'],
        
        'ร่างกาย'    :['ร่างกาย','กระดูกอ่อน','กราม','หัวไหล่','ทวาร','อึ','อุจจาระ','ลำไส้เล็ก','ตด','กลิ่นเต่า','ขี้ไคล','กายวิภาคศาสตร์','สมอง','ปมประสาท','หัวใจ','อัณฑะ','น้ำอสุจิ','น้ำลาย','ไขกระดูก','หายใจ','เรอ','จาม','สะโพก','หัวเข่า','ตับอ่อน','น้ำเหลือง','นัยน์ตา','ประสาท','ขมับ','กล่องเสียง','หัว','มือ','ขา','แขน','คอ','ตา','ปาก','กระดูก','กะโหลก','ฟัน','หู','อวัยวะ','ไส้ติ่ง','ประจำเดือน','องคชาต','ปอด','จมูก','ตับ','ดวงตา','ปัสสาวะ','กระดูกสันหลัง','โลหิต','ไหปลาร้า','เหงือก','มดลูก','เส้นเลือด','ลำไส้','ริมฝีปาก','เอว','คาง','หน้าผาก','รังไข่','เลือด','อสุจิ','ช่องคลอด','น้ำดี','ท้ายทอย','โยนี','น้ำนม','ไขสันหลัง','ขากรรไกร','น้ำเชื้อ',],
        
        'ความงาม'   :['ความงาม','ศัลยกรรม','กระ','ผิวหนัง','เล็บ','ผิว','หน้าอก','อก','สิว','เครื่องสำอาง','น้ำหอม','งาม','สวย','หล่อ','งดงาม','เครื่องประดับ','สปา','แต่งหน้า','เส้นผม','ตัดผม','ทำผม',],
        
        'สุขภาพ'     :['สุขภาพ','สายตา',   'สารอาหาร','สมุนไพร','ความเครียด','เครียด','ผอม','อ้วน','ลดน้ำหนัก','ลดความอ้วน','เพศสัมพันธ์','เล่นกล้าม'],
        'สายตา'     :['สายตาสั้น','สายตายาว','แว่นสายตา','แว่นตา','แว่น'],

        'สารอาหาร'  :['โปรตีน','ไขมัน','วิตามิน','กลูโคส','คาร์โบไฮเดรต',],

        'การแพทย์'   :['การแพทย์','อนามัย','เภสัช','ยา','ผ่าตัด','ทำแท้ง','รักษาตัว','แพทย์','ผู้ป่วย','หมอ','คนไข้','แพทยศาสตร์','คลินิก','พยาบาล','ปฐมพยาบาล','โรงพยาบาล','สภากาชาด',],
        
        'ชีววิทยา'    :['เนื้อเยื่อ','ชีวภาพ','เซลล์','พันธุกรรม','โครโมโซม','ชีวะ',],
        'จุลชีพ'      :['จุลชีพ','จุลินทรีย์','จุลชีววิทยา','เชื้อรา','รา','แบคทีเรีย','ไวรัส',],

        'คณิตศาสตร์'  :['คณิตศาสตร์','เรขาคณิต','เลข','คณิต','พีชคณิต','ฟังก์ชัน','สมการ','อสมการ','ลอการิทึม','ตรรกศาสตร์','แคลคูลัส','อนุกรม','ตัวเลข','เลขชี้กำลัง','เลขจำนวน','เลขคณิต','เลขโดด','จำนวนนับ','จำนวนเต็ม','จำนวนจริง','จำนวนจินตภาพ','จำนวนเชิงซ้อน','จำนวนตรรกยะ','จำนวนอตรรกยะ','ตัวแปร'],
        'เรขาคณิต'   :['เส้นผ่านศูนย์กลาง','เส้นผ่าศูนย์กลาง','วงกลม','รัศมี','วงรี','ลูกบาศก์','เส้นขนาน','สามเหลี่ยม','สี่เหลี่ยม''รัศมี','ปริมาตร','เส้นตรง','ระนาบ',],
        
        'การเงิน'    :['การเงิน','ธุรกิจ',   'เครดิต','พาณิชย์','ธนาคาร','กองทุน','ภาษี','ฐานะ','เงินกู้','โอน','บัญชี','ประมูล','ภาษีเงินได้','งก','งบ','คลัง','เงิน','รายได้','รายจ่าย','เงินออม','เงินเก็บ','คนรวย','รวย','ร่ำรวย','เศรษฐี','งบประมาณ','กู้ยืม','ลูกหนี้','ทุน','ดอกเบี้ย','มรดก','ทรัพย์สิน','หนี้สิน','ธนบัตร','เหรียญ','สตางค์','ดอลลาร์','เงินตรา','หุ้นส่วน','เงินสด','ตังค์'],
        'ธุรกิจ'      :['กำไร','ขาดทุน','ซื้อขาย','ค้าขาย','สินค้า','บริการ','ผู้บริโภค','ผลิตภัณฑ์','ยี่ห้อ','ต้นทุน','โฆษณา','การค้า','เครื่องหมายการค้า','กิจการ','ตลาด','ลูกค้า','ผู้บริโภค''ค้าขาย','ขายปลีก','ล้มละลาย',],
        
        'งาน'       :['งาน','ทำงาน','งานการ','พนักงาน','บริษัท','ออฟฟิศ','เจ้านาย','ลูกน้อง','ฝึกงาน','ว่างงาน','หัวหน้า','ผู้จัดการ','โบนัส','เงินเดือน','ค่าจ้าง','รับจ้าง','ลูกจ้าง','คนงาน','ลาออก','ไล่ออก','เกษียณอายุ','เกษียณ','อาชีพ','วิชาชีพ'],

        'เพาะปลูก'   :['เพาะปลูก','เกษตรกรรม','ปุ๋ย',   'ดิน','ดินร่วน','สวน','เพาะ','เคียว','วัชพืช','แร่ธาตุ','รดน้ำ',],
        'เกษตรกรรม' :['เกษตรกร','ฟาร์ม','เก็บเกี่ยว','ผลิตผล',],
        'ปุ๋ย'        :['ปุ๋ยคอก','ปุ๋ยหมัก','ปุ๋ยเคมี'],

        'ไม้ดอกไม้ประดับ'  :['ไม้ดอกไม้ประดับ','ไม้ดอก','ไม้ประดับ','ไม้พุ่ม','เบญจมาศ','กุหลาบ','ดอก','ดอกไม้','จำปา','มะลิ','จำปี','ราชพฤกษ์','ดาวเรือง','ดอกบัว','เฟิน','กล้วยไม้','ปาล์ม',],
        
        'ต้นไม้'      :['ต้นไม้','กิ่ง','ก้าน','ราก','ใบไม้','กาบ','เกสร','ฝัก','เถา','ไม้ยืนต้น','ไม้ล้มลุก'],
        
        'พืช'        :['หม้อข้าวหม้อแกงลิง','หญ้า'],
        
        'การเมือง'   :['การเมือง','การเมืองระหว่างประเทศ','ฝ่ายค้าน','หาเสียง','ปราศรัย','ประเทศ','รัฐ','รัฐบาล','ประชาธิปไตย','วุฒิสมาชิก','ประชาชน','พรรค','โหวต','มติ','นโยบาย','ผู้แทนราษฎร','อธิปไตย','กบฏ','คอมมิวนิสต์','ราชาธิปไตย','รัฐประหาร','สังคมนิยม','ปฏิรูป','ปฏิวัติ','เผด็จการ','ชาตินิยม','เสรีนิยม','อนุรักษนิยม','สงครามเย็น','ฟาสซิสต์','ทำเนียบ','สภา','รัฐสภา','คณะรัฐมนตรี','สภาผู้แทนราษฎร','วุฒิสภา','ปกครอง','ประชามติ','ลงคะแนน','คะแนนเสียง','นักการเมือง','สมาชิกวุฒิสภา','องคมนตรี','รัฐมนตรี','นายกรัฐมนตรี','นายก','ประมุข','ทูต','ผู้แทน',],
        'การเมืองระหว่างประเทศ'  :['พรมแดน','เขตแดน','สนธิสัญญา','อนุสัญญา''สหภาพ','คว่ำบาตร','เอกอัครราชทูต','มหาอำนาจ','สถานทูต','สันนิบาต','ภาคี','สมัชชา','การต่างประเทศ',],

        'การปกครอง' :['การปกครอง','สมบูรณาญาสิทธิราชย์','อำนาจ','อิทธิพล','จักรพรรดิ','อาณาจักร','จักรวรรดิ','ราชอาณาจักร','ประเทศชาติ','นครรัฐ','ทาส','ยึดอำนาจ','ประชากร'],
        
        'สังคม'      :['สังคม' ,'วัฒนธรรม','ธรรมเนียม','คติ','วิถีชีวิต','ภูมิปัญญา','ประเพณี','ค่านิยม','มารยาท','ภาพพจน์','ชื่อเสียง','ภาพลักษณ์'],
        
        'ศาสนา'     :['ศาสนา','พุทธ','คริสต์','อิสลาม',   'พราหมณ์','คัมภีร์','สวรรค์','ลัทธิ','วิหาร','เทวสถาน','นักบุญ','แม่ชี','ชี','โบสถ์','สวด','นรก','สาวก','พรหม','นารายณ์','พระเจ้า','เทพเจ้า','เทพ','เทวดา','ศาสนิกชน','พระผู้เป็นเจ้า','ล้างบาป','นักบวช','ซิกข์','บาป'],
        'พุทธ'       :['วันพระ','สำนักสงฆ์','พระ','พระพุทธเจ้า','สงฆ์','อุปสมบท','ออกบวช','วิสาขบูชา','ภิกษุ','ภิกษุณี','สามเณร','หลวงพ่อ','เจ้าอาวาส','พระครู','เจ้าคณะ','เถรวาท','มหายาน','พระพุทธองค์','กุศล','สักการะ','อรรถกถา','อาราม','เถระ','สมาธิ','อุโบสถ','เจดีย์','จำพรรษา','มุนี','สมโภช','เถร','เมตตา','กรรม','ทำบุญ','นมัสการ','มหานิกาย','ปรินิพพาน','ธรรมะ','กุฏิ','ปฏิบัติธรรม','ตรัสรู้','สังคายนา','กรรมฐาน','วิสุงคามสีมา','พระประธาน','พุทธกาล','สุตตันตปิฎก','ทุกข์','นักพรต','ปิฎก','อภิธรรม','เทศนา','พุทธศาสนิกชน','วิปัสสนา','นิมนต์','แม่พระ','กิเลส','ฆราวาส','เทศน์','ธุดงค์','รับศีล','นิพพาน','มรรค','ธรรมกาย','ปัญจวัคคีย์','สิทธัตถะ','โสดาบัน','ธรรม'],
        'คริสต์'      :['คริสเตียน','เยซู','โมเสส','กางเขน','โรมันคาทอลิก','คริสตจักร','คาทอลิก','โปรเตสแตนต์',],
        'อิสลาม'     :['อัลกุรอาน','มุสลิม','มัสยิด','สุเหร่า','อิหม่าม'],
        
        'เคมี'       :['ตารางธาตุ','สารประกอบ',   'ธาตุ','สาร','ออกซิเดชัน','สูตรเคมี','ไอออน','พันธะ','สารละลาย','กรด','ด่าง','ปฏิกิริยา',],
        'ตารางธาตุ'  :['ไฮโดรเจน','ฮีเลียม','ลิเธียม','โบรอน','คาร์บอน','ไนโตรเจน','ออกซิเจน','โซเดียม','แมกนีเซียม','อะลูมิเนียม','ซิลิคอน','ฟอสฟอรัส','กำมะถัน','คลอรีน','อาร์กอน','โพแทสเซียม','แคลเซียม','โครเมียม','แมงกานีส','เหล็ก','นิกเกิล','ทองแดง','สังกะสี','ดีบุก','ไอโอดีน','ซีนอน','ทังสเตน','แพลทินัม','ปรอท','ตะกั่ว'],
        'สารประกอบ' :['คาร์บอนไดออกไซด์','ฟอสเฟต','แอมโมเนีย','คาร์บอเนต','ไฮโดรคาร์บอน',],
        
        'วัสดุ'       :['วัสดุ','กระจก','เหล็กกล้า','ทองเหลือง','พลาสติก','โฟม','โลหะ','สำริด','หินอ่อน','ยาง'],    
        
        'ก่อสร้าง'    :['ก่อสร้าง','สิ่งก่อสร้าง','โยธา','สถาปัตยกรรม','สถาปนิก','ซีเมนต์','รื้อถอน','ต่อเติม','เสา','ผนัง','เพดาน','บันได','หลังคา','หน้าต่าง','คาน','อิฐ','ปูน','ถือปูน''เพดาน','ประตู','คอนกรีต','กระเบื้อง','คอนกรีตเสริมเหล็ก',],
        
        'กฎหมาย'    :['กฎหมาย','สิทธิ','ลิขสิทธิ์','จดทะเบียน','ขึ้นทะเบียน','บทบัญญัติ','ประมวลกฎหมาย','กฤษฎีกา','กฎบัตร','คดี','นิติศาสตร์','ข้อบังคับ','คุก','ตุลาการ','ผู้พิพากษา','อัยการ','ทนายความ','ประหารชีวิต','จับกุม','ส่งตัว','คุมขัง''ประหารชีวิต','ลงโทษ','จำคุก','ประหาร','เนรเทศ','ตำรวจ','พลเรือน','ข้อหา','เรือนจำ','ราชกิจจานุเบกษา','พระราชบัญญัติ','สิทธิมนุษยชน','รัฐธรรมนูญ','มาตรา','พระราชกฤษฎีกา','พระราชกำหนด','หมิ่นประมาท','จำเลย','พิพากษา','พยาน','พยานหลักฐาน','คำพิพากษา','อาญา','กฎหมายแพ่ง','สอบสวน',],
        
        'ราชวงศ์'    :['ราชวงศ์','หลวง','พระราชพิธี','จักรี','พระเจ้าอยู่หัว','พระนางเจ้า','อภิเษกสมรส','ราชบัลลังก์','ราชาภิเษก','ครองราชสมบัติ','สละราชสมบัติ','สืบราชสมบัติ','บัลลังก์','ราชสมบัติ','เฉลิมพระชนมพรรษา','รัชกาล','โอรส','ธิดา','มเหสี','ชายา','เชษฐา','อนุชา','สวามี','นัดดา','ชนนี','ภคินี','ชนก','ขนิษฐา','อัครมเหสี','กษัตริย์','เจ้าฟ้า','ราชา','รัชทายาท','ราชินี','มกุฎราชกุมาร','พระสนม','เจ้าจอม',],
        
        'อดีต'       :['อดีต','สมัย','ยุค','วัยเด็ก','สมัยเก่า',],
        
        'เครื่องใช้ไฟฟ้า'   :['เครื่องใช้ไฟฟ้า','จอ','ตู้เย็น','พัดลม','ลำโพง','วิทยุ',     'แอร์','เครื่องปรับอากาศ','เครื่องทำนำ้อุ่น','เครื่องซักผ้า','เครื่องอบผ้า','เครื่องดูดฝุ่น',               'เครื่องบันทึกเสียง','โทรทัศน์','ไมโครเวฟ','หม้อหุงข้าว','เตาไฟฟ้า','เตารีด','ไมโครโฟน','ไดร์เป่าผม',],
        
        'เทพนิยาย'   :['เทพนิยาย','มังกร','เงือก','แม่มด','นางฟ้า','เทพธิดา','ปกรณัม','ตำนาน','นาค','ครุฑ',],
        
        'สิ่งลี้ลับ'     :['สิ่งลี้ลับ','ผี','กระสือ','ผีดิบ','ปีศาจ','ภูติ','วิญญาณ','ลึกลับ','พลังจิต','อสูร','ปิศาจ','ไสย','ไสยศาสตร์','คุณไสย','คาถา','สาป','เวทมนตร์','เวท','เครื่องราง','อาถรรพ์','พิธีกรรม',],
        
        'เดินทาง'    :['เดินทาง','จราจร','จุดหมาย','จุดหมายปลายทาง','หนังสือเดินทาง','ขนส่ง','การขนส่งมวลชน','เดินรถ','สถานี','ชานชาลา','ทางด่วน','สัญจร','เส้นทาง','เดินเรือ','ยานพาหนะ','พาหนะ','รถราง','รถบรรทุก','รถจักรยานยนต์','รถประจำทาง','รถโดยสารประจำทาง','โดยสาร','รถเมล์','รถสองแถว','เรือ','รถ','จักรยาน','แท็กซี่','รถตู้','มอเตอร์ไซค์','เครื่องบิน','รถไฟ','รถยนต์','ท่าอากาศยาน','รถไฟฟ้า','ผู้โดยสาร','สนามบิน','อากาศยาน','ถนน',],
        
        'ภาษา'      :['ภาษา','คำ','อักษร','อักษรศาสตร์','สำเนียง','วรรณศิลป์','ศัพท์','ศัพท์บัญญัติ','ประโยค','พยัญชนะ','วลี','อักขระ','พยางค์','รากศัพท์','ไวยากรณ์','กริยา','พจนานุกรม','ภาษาถิ่น','วรรณยุกต์','อุปมา','โครงเรื่อง','ร้อยกรอง','โคลง','กลอน','เนื้อความ','ตัวหนังสือ','ร้อยแก้ว','ทับศัพท์','ลายมือ','ตัวสะกด','สันสกฤต',],
        
        'ต่างประเทศ' :['ต่างประเทศ','ยุโรป','อเมริกา',       'สากล','ญี่ปุ่น','จีน','เกาหลี','รัสเซีย','ออสเตรเลีย','นิวซีแลนด์','ตุรกี','อียิปต์','สเปน','บราซิล',        'มาเลเซีย','พม่า','กัมพูชา','เขมร','ลาว','สิงคโปร์','เวียดนาม','ฟิลิปปินส์','อินโดนีเซีย','อินเดีย','เดนมาร์ก','ไต้หวัน','มอญ','ชวา','มลายู','ญวน','แขก','ขอม','ลังกา','ฝรั่ง','ดัตช์','ตะวันออกกลาง','ตะวันออกไกล','ตะวันออกใกล้',],
        'ยุโรป'      :['กรีซ','นอร์เวย์','เนเธอร์แลนด์','เบลเยียม','โปรตุเกส','ฝรั่งเศส','ฟินแลนด์','เยอรมนี','สวิตเซอร์แลนด์','สวิส','สวีเดน','สหราชอาณาจักร','อังกฤษ','ออสเตรีย','อิตาลี',],
        'เกาหลี'     :['เกาหลีเหนือ','เกาหลีใต้'],
        'อเมริกา'    :['สหรัฐอเมริกา','อเมริกัน'],
        'เยอรมนี'    :['เยอรมัน',],
        
        'ฟิสิกส์'      :['ควอนตัม','มวล','กลศาสตร์','แรง','ของไหล','ความโน้มถ่วง','คลื่นแม่เหล็กไฟฟ้า','ไฟฟ้าสถิต','แรงดึงดูด','แม่เหล็ก','สนามแม่เหล็ก',],
        
        'ดาราศาสตร์' :['ดาวเคราะห์','ดาวฤกษ์','โลก','อวกาศ','จักรวาล','ทางช้างเผือก','โคจร','ระบบสุริยะ','เนบิวลา','ปีแสง','ดาว','จรวด','ยานอวกาศ','เอกภพ','ดาวหาง','พลูโต','อุกกาบาต','สุริยุปราคา','กล้องโทรทรรศน์','เนปจูน','จันทรุปราคา',],
        
        'อะตอม'     :['อนุภาค','โมเลกุล','อิเล็กตรอน','ประจุ','นิวเคลียส','นิวตรอน','ปฏิกรณ์','สสาร','โปรตอน',],
        
        'ชีวิตคู่'      :['ชีวิตคู่','คู่ใจ','คู่ครอง','สามี','ภรรยา','ภริยา','เมีย','ที่รัก','จดทะเบียนสมรส','งานแต่งงาน','แต่งงาน','หย่า','ดูใจ','วิวาห์','เจ้าสาว','คู่สมรส','เลิกรา','คู่หมั้น',],
        
        'เลี้ยงเด็ก'   :['เลี้ยงเด็ก','ตั้งครรภ์','คลอด','ครรภ์','มีลูก','ทารก','เด็ก','เลี้ยงดู','ผู้ปกครอง','ลูกหลาน','ลูก','คลอดลูก','ตั้งท้อง','ซน','เด็กชาย','เด็กหญิง'],
        
        'ครอบครัว'   :['ครอบครัว','พ่อแม่','พ่อ','แม่','มารดา','ตระกูล','สืบเชื้อสาย','สายเลือด','เชื้อสาย','แม่ผัว','สะใภ้','พ่อตา','พี่น้อง','ลูกพี่ลูกน้อง','ญาติ','ทวด','ทายาท','หลาน','ลุง','ยาย','บุญธรรม','บุตรบุญธรรม','ลูกสาว', 'ลูกชาย'],
        
        'ความรัก'    :['ความรัก','รัก','จีบ','กอด','จูบ','คิดถึง','ผูกพัน','สารภาพรัก','คลุมถุงชน','คนรัก','มีชู้','แฟน','คบหา','เสน่ห์','โสด','อกหัก','กามเทพ','โรแมนติก'],
        
        'ประวัติศาสตร์':['ประวัติศาสตร์','ประวัติ','โบราณสถาน','อารยธรรม','โบราณคดี','โบราณวัตถุ','พงศาวดาร','จดหมายเหตุ','จารึก','โรมัน','โบราณ','พิพิธภัณฑ์','ศตวรรษ','ทศวรรษ','เหตุการณ์','ร่วมสมัย',],
        
        'ภูมิศาสตร์'   :['ภูมิศาสตร์','ขั้วโลก',   'ภูมิประเทศ','ภูมิอากาศ','มหาสมุทร','ทวีป','สมุทร','เมริเดียน','ที่ราบ','ลุ่ม','ลุ่มน้ำ','ดินดอนสามเหลี่ยม','ภูมิภาค','เปลือกโลก','ที่ราบสูง','ลูกโลก',],
        'ขั้วโลก'     :['ขั้วโลกเหนือ','ขั้วโลกใต้','ภูเขาน้ำแข็ง'],

        'ธรณีวิทยา'   :['ธรณีวิทยา','หิน','ทราย','โคลน','หินทราย','กรวด','ธรณี','ไดโนเสาร์','ซากดึกดำบรรพ์',],
        
        'ธรรมชาติ'   :['ธรรมชาติ','แม่น้ำ','เทือกเขา','ภูเขา','ผา','ดอย','ทะเลทราย','เกาะ','ทะเลสาบ','ลำธาร','ป่าดิบ','ป่าดงดิบ','ป่าทึบ','ป่าโปร่ง','ถ้ำ','น้ำตก','น้ำค้าง','ฝน','หิมะ','หมอก','ทะเล','ลม','เมฆ','สายฟ้า','ทรัพยากรธรรมชาติ'],
        
        'ภาพยนตร์'   :['หนัง','ถ่ายภาพยนตร์','บทพากย์','พากย์หนัง','พากย์',],
        
        'อุตสาหกรรม' :['อุตสาหกรรม','โรงงาน','แรงงาน',],
        
        'ปรัชญา'     :['ปรัชญา','คุณธรรม','จริยธรรม','มนุษยธรรม',],
        
        'จิตใจ'      :['จิตใจ','จิต','อารมณ์','นิสัย','รสนิยม',],
        
        'บุคลิกภาพ'   :['บุคลิกภาพ','น้ำเสียง',],
        
        'ราชการ'    :['ราชการ','รับราชการ','ข้าราชการ','ภาษาราชการ','เอกสารราชการ'],
        
        'การปกครองส่วนท้องถิ่น' :['การปกครองส่วนท้องถิ่น','ตำบล','แขวง','เขต','จังหวัด','อำเภอ','ผู้ว่าราชการจังหวัด','หมู่บ้าน','ชุมชน','เทศบาล','ส่วนท้องถิ่น','กิ่งอำเภอ','สุขาภิบาล','ส่วนภูมิภาค','นายอำเภอ','กำนัน','ปลัด','ผู้ใหญ่บ้าน','นายกเทศมนตรี',],   
        
        'ศาสตร์'     :['ศาสตร์','วิทยาการ','เวชศาสตร์','ภาษาศาสตร์','พฤกษศาสตร์','รัฐศาสตร์','มนุษยศาสตร์','นิเทศศาสตร์','สังคมศาสตร์','ศิลปศาสตร์','พาณิชยศาสตร์','สถาปัตยกรรมศาสตร์',],
        
        'การแข่งขัน'  :['การแข่งขัน','ทีม','คู่แข่ง','คู่ปรับ','คัดเลือก','ประกวด','กรรมการ','ประลอง','ถ้วยรางวัล','รางวัล','ชนะ','เอาชนะ'],
        
        'มายากล'    :['มายากล','มายา','กล','ภาพลวงตา',],
        
        'การทหาร'   :['การทหาร','ทหาร','ทหารผ่านศึก','ยุทโธปกรณ์','สงคราม','ยุทธการ','สงครามโลก','กองทัพ','ทัพ','แม่ทัพ','เชลย','บัญชาการ','เสนาธิการ','ฝูงบิน','เดินทัพ','ถอยทัพ','สมรภูมิ','ขีปนาวุธ','ยุทธวิธี','สนามรบ','ไพร่พล','กองพล','เรือรบ','ข้าศึก','นาวิกโยธิน',],
        
        'รังสี'       :['รังสี','กัมมันตภาพรังสี','ไอโซโทป','กัมมันตรังสี','สเปกตรัม','ความยาวคลื่น','นิวเคลียร์','รังสีวิทยา','แกมมา','แอลฟา','การแผ่รังสี',],
        
        'พลังงาน'    :['พลังงาน','เชื้อเพลิง','ไฟฟ้า','ถ่านหิน','น้ำมัน','น้ำมันดิบ',],
        
        'สิ่งปลูกสร้าง' :['สิ่งปลูกสร้าง','ปราสาท','อุโมงค์','อาคาร','ตึก','ศาลา','เรือน','คอนโดมิเนียม','อนุสาวรีย์','ตำหนัก','คฤหาสน์','หอประชุม','วัง','สะพาน','เขื่อน',],
        
        'ชีวิต'       :['ชีวิต','เวลา','โอกาส','คุณค่า','ตัดสินใจ','อายุ','วัย','ผู้ใหญ่','มีอายุ','เกียรติ',],
        
        'ความขัดแย้ง' :['ความขัดแย้ง','ขัดแย้ง','อริ','จลาจล','ชุมนุม','ประท้วง','ต่อต้าน','ชีวประวัติ','ต่อสู้','ปะทะ','โจมตี','รุกราน','พิชิต','คุกคาม','ฆ่า','สังหาร'],
        
        'ของเล่น'    :['ของเล่น','เกม','การ์ด','ไพ่','ตุ๊กตา','เครื่องเล่น','การละเล่น',],
        
        'ปริศนา'     :['ปริศนา','สืบสวน','สันนิษฐาน','สมมติฐาน','จิตวิทยา','รหัส',],
        
        'อากาศ'     :['อากาศ','อุณหภูมิ','มรสุม','หนาว','แห้งแล้ง','อุตุนิยมวิทยา'],
        
        'เศรษฐกิจ'   :['เศรษฐกิจ','ราคา','มูลค่า','เศรษฐศาสตร์','เงินเฟ้อ','ทุนนิยม',],
        
        'ส่วนตัว'     :['ส่วนตัว','ลับ'],
        
        'เมือง'      :['เมือง','เมืองหลวง','กรุง','นคร','บ้านเรือน','ครัวเรือน','หลังคาเรือน','ตัวเมือง','ปริมณฑล',],
        
        'ทางการ'    :['ทางการ','พิธีการ',],
        
        'เอกสาร'    :['เอกสาร','ข้อความ','จดหมาย',],
        
        'สถิติ'       :['สถิติ','กราฟ','แผนภูมิ',],
        
        'สาระ'      :['สาระ','ข้อมูล',],
        
        'อิเล็กทรอนิกส์':['อิเล็กทรอนิกส์','ทรานซิสเตอร์','มอเตอร์','แบตเตอรี่','วงจร','มิเตอร์','สวิตช์',],
        
        'รถยนต์'     :['รถยนต์','เครื่องยนต์','เกียร์','ตัวถัง','แรงม้า','ดีเซล','ลูกสูบ','เบนซิน',],
        
        'อาสา'      :['อาสา','มูลนิธิ','อาสาสมัคร',],
        
        'แปลก'      :['แปลก','ประหลาด','พิศวง',],
        
        'พฤติกรรม'   :['พฤติกรรม','ดุร้าย','ก้าวร้าว','สุภาพ'],
        
        'ของขวัญ'    :['ของขวัญ'],
        
        'อนาคต'     :['อนาคต','ทำนาย','พยากรณ์',],
        
        'เทคโนโลยี'  :['เทคโนโลยี','หุ่นยนต์','นวัตกรรม'],
        
        'วิศวกรรม'   :['วิศวกรรม','วิศวกร','เครื่องจักร','กลไก','เฟือง','วิศวกรรมศาสตร์',]
    }

    return word_dict
